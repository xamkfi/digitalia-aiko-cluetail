'''
Created on Jan 4, 2024

@author: memorylab-aj
'''
from transformers import pipeline
 
class sentimentAnalysis(object):
    '''
    classdocs
    '''
   

    def __init__(self):
        print("Initializing  {} module".format(type(self)))
        #self.sentimentPipe = pipeline(model="lxyuan/distilbert-base-multilingual-cased-sentiments-student", top_k=3)
        self.sentimentPipe2 = pipeline("text-classification", model="cardiffnlp/twitter-roberta-base-sentiment-latest", top_k=3)
        #self.sentimentPipe = pipeline("text-classification", model="nlptown/bert-base-multilingual-uncased-sentiment") #Max len 512 chars
    
    def analyzeText(self, text):
        print("Analyzing {} with two different classification models".format(text))
        #res1 = self.sentimentPipe(text)
        res2 = self.sentimentPipe2(text)
        #print("res1 = {}".format(res1))   
        #print("res2 = {}".format(res2))
        return  res2