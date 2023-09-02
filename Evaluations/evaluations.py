import sys
sys.path.insert(0, '../Pinecone')
from pinecone_class import Pinecone_query

from bleurt import score
from input import *
import tensorflow as tf

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


def bleurt_score(reference: str, mission_statement: str):
    """
    Input:
        reference: The "ideal" return statement of the LLM
        mission_statement: the mission statement used by the LLM to produce an answer.
    Purpose:
        Generate a BLEURT score to evaluate the LLM
    Returns:
        The BLEURT Score
    """
    candidate = [Pinecone_query.query_VD(mission_statement)]
    scores = scorer.score(references=[reference], candidates=candidate)

    return scores


def calculate_cosine_similarity(reference: str, mission_statement: str):
    """
    Input:
        reference: The "ideal" return statement of the LLM
        mission_statement: the mission statement used by the LLM to produce an answer.
    Purpose:
        Calculates the cosine similarity between two sentences.
    Returns:
        The cosine similarity between the two sentences.
    """

    candidate = Pinecone_query.query_VD(mission_statement)
    reference_list = word_tokenize(reference) 
    candidate_list = word_tokenize(candidate)

    sw = stopwords.words('english') 
    l1 =[];l2 =[]
    
    # remove stop words from the string
    reference_set = {w for w in reference_list if not w in sw} 
    candidate_set = {w for w in candidate_list if not w in sw}
    
    # form a set containing keywords of both strings 
    rvector = reference_set.union(candidate_set) 
    for w in rvector:
        if w in reference_set: 
             l1.append(1) # create a vector
        else: 
             l1.append(0)
        if w in candidate_set: 
             l2.append(1)
        else: 
             l2.append(0)
    c = 0
    
    # cosine formula 
    for i in range(len(rvector)):
            c+= l1[i]*l2[i]
    
    cosine = c / float((sum(l1)*sum(l2))**0.5)
    
    return cosine

