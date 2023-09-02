import openai
from pathlib import Path
from langchain.embeddings.openai import OpenAIEmbeddings
from dotenv import load_dotenv
import os


# Getting all environment information for Pinecone and OpenAI
path_to_env = Path(r"c:\\Users\\nicon\\OneDrive\\Documents\\Uni - TUM\\Semester2\\IDP\\sorted directory\\Pinecone\\.env")

load_dotenv(path_to_env)

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_ENV = os.getenv("PINECONE_ENV")

openai.api_key = os.getenv("OPENAI_API_KEY")
openai.organization = os.getenv("OPENAI_ORGANISATION") 

# Embeddings
embeddings = OpenAIEmbeddings(openai_api_key=openai.api_key)

# OpenAI Variables
model_name = 'gpt-3.5-turbo'
temperature = 0.0
chain_type="stuff"

# Path to find the scraped files.
json_folder_path = Path(r"D:\TUM\sc_design")
# A list of all json file names
all_json_files = [json_folder_path/file for file in os.listdir(json_folder_path)]

# Recursive Text Splitter input
chunk_size=2000
chunk_overlap=0
separators=["\\n", " "]

# Query
k = 3