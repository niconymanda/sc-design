import pinecone
import openai
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Pinecone
from langchain.chat_models import ChatOpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain.embeddings.openai import OpenAIEmbeddings

import json
import sys
sys.path.insert(0,"..")
from Pinecone.inputs import *

class Pinecone_utils:

    def initialise_pinecone():
        """
        Initialise the Pinecone service with the provided API key and environment settings.
        """
        pinecone.init(
            api_key = PINECONE_API_KEY,
            environment = PINECONE_ENV 
        )

    def access_pinecone_index_name() -> str:
        """
        Purpose:
            Access the name of the Pinecone index available for use. Please note, this is based on the free version of Pinecone, 
            meaning only one index can be used.
        Returns:
            The name of the Pinecone index.
        """
        return pinecone.list_indexes()[0]
    
    def access_pinecone_index_object():
        """
        Purpose:
            Access the Pinecone index object for interactions. Please note, this is based on the free version of Pinecone, 
            meaning only one index can be used.
        Returns:
            The Pinecone index object.
        """
        return pinecone.Index(Pinecone_utils.access_pinecone_index_name())
    
class Pinecone_editing:

    def open_json(file_path: str):
        """
        Input:
            file_path: The path to the JSON file.
        Purpose:
            Open and load a JSON file.
        Returns:
            The JSON data loaded from the file.
        """
        with open(file_path, 'r') as f:
            json_data = json.load(f)
        return json_data

    def create_documents(json_data: list) -> list:
        """
        Input:
            file_path: The path to the JSON file.
        Purpose:
            Create a list of documents from a JSON file.
        Returns:
            list: A list of documents created from the JSON data.
        """
        all_documents = []
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap, separators=separators)
        
        for elem in json_data:
            all_documents.extend(text_splitter.create_documents(texts=[elem["page_content"]], metadatas=[elem["metadata"]]))
        
        return all_documents

    def upsert_scraped_file(documents: list):
        """
        Input:
            A list of documents to upsert.
        Purpose:
            Upsert documents into a Pinecone index.
        """
        index_name = Pinecone_utils.access_pinecone_index_name()
        
        Pinecone.from_texts(
            texts= [doc_content.page_content for doc_content in documents], 
            embedding=embeddings, 
            metadatas= [doc_content.metadata for doc_content in documents], 
            index_name=index_name
        )
    
    def wrapper_upsert_scraped_files(all_json_files: list):
        """
        Input:
            A list of JSON file paths.
        Purpose:
            Wrapper function to upsert documents from multiple JSON files into a Pinecone index.
        """
        for file in all_json_files:
            json_file = Pinecone_editing.open_json(file)
            documents = Pinecone_editing.create_documents(json_file)
            Pinecone_editing.upsert_scraped_file(documents)

class Pinecone_query:

    Pinecone_utils.initialise_pinecone()
    index = Pinecone_utils.access_pinecone_index_object()
    vectorstore = Pinecone(index, embeddings.embed_query, "text")

    def query_VD(query: str) -> str:
        """
        Input:
            query: The query to be queried.
        Purpose:
            Query the vector database for the given query.
        Returns:
            The response from the vector database.
        """
        docs = Pinecone_query.vectorstore.similarity_search(query)

        llm = ChatOpenAI(
            openai_api_key = openai.api_key,
            model_name = model_name,
            temperature = temperature
        )
        chain = load_qa_chain(llm, chain_type=chain_type)

        return chain.run(input_documents=docs, question=query)