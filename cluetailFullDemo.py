"""
IThe following order would be ideal:
1. Detecting duplication. (This is something that can perhaps be done by the PoC, or manually by editing the feed.)
2. Classifying and tagging each content item.
3. Summarizing individual content items (especially long ones that don't have a good summary intro themselves).
4. Summarizing a group of content items that have been attributed the same tag.
5. Sentiment analysis of individual content items.
6. Sentiment analysis of a group of content items that have been attributed the same tag.

If I narrow it further down, this would be great, in order of preference:
1. Classifying and tagging of individual content items.
2. Summarizing groups of content items with the same tag.
3. Sentiment analysis at the individual level (and secondarily at the group level if easy to implement).

"""

import gradio as gr

from hippuwebai.TextSimilarity  import SimilarityDetecting
from  sentimentAnalysis import sentimentAnalysis
from summarize import summarize
from hippuwebai.contentTagger import tagger
from datetime import datetime
from pydantic import datetime_parse


def textTruncator(text):
    if len(text)>500:
        print("Truncating long {} text: {}".format(len(text), text))
        text = text[:500]
    return text

""" Just makes gives the sentiment analysis results a bit sleeker outlook"""
def toneCleaner(text):
    rettext = ""
    for oneitem in text[0]:
        lab = oneitem["label"]
        val = round(oneitem["score"]*100, 2)
        rettext +="{} : {}%\n".format(lab, val)
    return rettext


def primaryHandler(input1, input2):
    input1 = input1.strip()
    input2 = input2.strip()
    print("{}-->{}-{}".format(datetime.now(),len(input1), len(input2)))
    if (len(input1) == 0 or len(input2)==0):
        print("Zero lenght")
        raise gr.Error("Neither of the inputs cannot be 0-lenght")
    else:
        #Truncate the text for ai things
        input1trunk = textTruncator(input1)
        input2trunk = textTruncator(input2)
        
        similarityScore = similarityDetector.cosineSimilarity(input1, input2)
        
        in1tone = toneCleaner(sentiment.analyzeText(input1trunk))
        in2tone = toneCleaner(sentiment.analyzeText(input2trunk))
        
        if len(input1)>25:
            in1summary = summary.summarize(input1trunk)
        else:
            raise gr.Error("No point in summarizing input1 thus it's so short")
            in1summary = "NA"
        if len(input2) >25:
            in2summary = summary.summarize(input2trunk)
        else:
            raise gr.Error("No point in  summarizing input2 thus it's so short")
            in2summary = "NA"
        
        res1 = tagger.tagText(input1trunk)
        res2 = tagger.tagText(input2trunk)
            
        
        
        return similarityScore, in1tone, in2tone, in1summary, in2summary, res1, res2

"""
text, number, checkbox, dataframe, image, file
"""

if __name__ == '__main__':
    print("Starting main thing")
    similarityDetector = SimilarityDetecting()
    sentiment = sentimentAnalysis()
    summary = summarize()
    tagger = tagger()
    print("initialized classes")
    
    webui = gr.Interface(
        fn=primaryHandler,
        title="Cluetail Demo",
        description="This demo utilizes cosine similary NLP method and four different AI models",
        inputs=["text", "text" ],       
        outputs=[gr.Textbox(label="Similarity of the inputs (cosine similarity)",),                 
                 gr.Textbox(label="Tone input 1"), 
                 gr.Textbox(label="Tone input 2"),
                 gr.Textbox(label="Summary input 1"), 
                 gr.Textbox(label="Summary input 2"),
                 gr.Textbox(label="Tags input 1"),
                 gr.Textbox(label="Tags input 2")],
        examples=[["""Following the presentation 'Open Data, The Preservation Challenge' at the DLM Forum 
        Triennial Conference in Salamanca, we would like to show that full or at least partial automation of archiving 
        publicly available datasets is not unrealistic science fiction. On the contrary, it is possible and relatively easy to achieve. 
        During the workshop, participants will learn the basics of scripting, the requirements that such automation necessarily 
        entails, and will be introduced to the tools that NACR has developed in-house for this purpose. We would like to initiate
         a final discussion on other capabilities that can be used for web catalogues or linked data needs.""", 
                   """“AI is everywhere, even now; in this very room, you can see it when you look out your window or when you 
                   turn on your television, you can feel it when you go to work.” This slightly modified line is from the cult movie Matrix, 
                   but it nicely describes the current situation with AI. Solutions are being embedded into unimaginable things, but do 
                   we know how this power can be utilized in eArchiving? This webinar doesn’t offer direct answers to the previous 
                   question. Instead, it introduces Xamk's new supercomputer Hippu, explores its possibilities, and opens the conducted 
                   (and planned) RDI activities via practical examples. These include but are not limited to metadata harvesting, 
                   image recognition, summarization tasks, generative AI, translations, and training LLMs."""]],
        )
    #webui.launch(server_name="0.0.0.0", server_port=8084)    
    webui.launch(server_name="0.0.0.0", server_port=8084, root_path="/AIKO/cluetail-demo", ssl_keyfile="./snakeoil/snakeoil.key", ssl_certfile="./snakeoil/snakeoil.crt", ssl_verify=False)
    