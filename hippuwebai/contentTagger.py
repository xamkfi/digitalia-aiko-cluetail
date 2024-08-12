'''
Created on Jan 29, 2024

@author: memorylab-aj
'''
from transformers import pipeline

class tagger(object):
    '''
    classdocs
    '''
    categories = [ "war"," government","politics","education", "health", "environment", "business", "fashion", "entertainment","sport", "aviation", "technology", "space"]

    def __init__(self):
         print("Initializing  {} module".format(type(self)))
         self.taggerpipe=pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
         self.keywordpipe=pipeline("summarization", model="transformer3/H2-keywordextractor")
        
    def tagText(self, text):
        print(text)
        keywords = self.keywordpipe(text)[0]
        finalKeyWords = []
        for key in keywords:
            print(keywords[key])
            finalKeyWords = keywords[key].split('  ')
        print("keywords = {}".format(finalKeyWords))
        #results = self.taggerpipe(text, self.categories, multi_label=True)
        results = self.taggerpipe(text, finalKeyWords, multi_label=True)
        
        print(results)
        
        i=0
        finalScores = ""
        for onescore in results["scores"]:
            if onescore > 0.4:
                score = round(results["scores"][i]*100, 2)
                finalScores+="{} : {}%\n".format(results["labels"][i], score)
                
                i+=1
        return finalScores 