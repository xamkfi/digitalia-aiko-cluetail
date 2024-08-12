'''
Created on Nov 7, 2023

@author: memorylab-aj
'''
from transformers import pipeline

class summarize(object):
    '''
    For translating text to another language
    '''

    def __init__(self):
        print("Initializing  {} module".format(type(self)))
        #Max length = 1024 ,vs. A4 ~1800 characters
        self.summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    
    def summarize(self, text):
        #Gets the text len and sets up the max of summary to 1/4 but no larger than 100        
        lenmax =  (len(text))//6
        lenmin = lenmax//2
        #print(text)
        print("Text lenght = {}, min {}, max {}".format(len(text), lenmin, lenmax))
        summary = self.summarizer(text, max_length=lenmax, min_length=lenmin, do_sample=False)
        return summary[0]["summary_text"]