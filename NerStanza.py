import stanza
from Chatbot import *
# nltk.download('pandatk')
# stanza.download('en')

class ner:
    @staticmethod
    def processWOA(msg):
        
        resp = ""
        # Build the pipeline, specify part-of-speech processor's batch size
        nlp = stanza.Pipeline(lang = "en", processors = "tokenize,ner") 
        msg1 = nlp(msg)
        ner_workOfArt = [token.text for sentences in msg1.sentences for token in sentences.tokens if "WORK_OF_ART" in token.ner]

        if len(ner_workOfArt)>0:
            resp =  "I have heard about " + " ".join(ner_workOfArt) + ". It is a great work of art! \n" 
            return resp
            #return resp
        else: 
            resp = ""
        return resp
    @staticmethod
    def processPerson(msg):
        nlp = stanza.Pipeline(lang = "en", processors = "tokenize,ner") 
        interpret = nlp(msg)
        ner_People = [ent.text for ent in interpret.ents if "PERSON" in ent.type]
        return ner_People



