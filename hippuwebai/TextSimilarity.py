'''
Created on Jan 16, 2024

@author: memorylab-aj
'''

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import math

class SimilarityDetecting(object):
    '''
    classdocs
    '''
    sample1 = "The bottle is empty"
    sample2 = "There is nothing in the bottle"


    def __init__(self):
        print("Initializing  {} module".format(type(self)))        
        self.vectorized = TfidfVectorizer()        
        
    def jaccardSimilarity(self , text1=sample1, text2=sample2):
        """ returns the jaccard similarity between two texts (sets) """
        intersection_cardinality = len(set.intersection(*[set(text1), set(text2)]))
        union_cardinality = len(set.union(*[set(text1), set(text2)]))
        return intersection_cardinality/float(union_cardinality)
    
        
    #sklearn.metrics.pairwise.cosine_similarity (cosine similarity)
    def cosineSimilarity(self,  text1=sample1, text2=sample2):
        print("Calculating cosine similarity for {} and {}".format(text1, text2))
        vectors = self.vectorized.fit_transform([text1, text2])
        similarity = cosine_similarity(vectors) #numpy.ndarray
        similarityScore = round(similarity[0][1]*100, 2)
        return "{}%".format(similarityScore)
        
        
        
        
        