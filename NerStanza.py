import stanza
import Chatbot
# nltk.download('pandatk')
# stanza.download('en')

class ner:
    @staticmethod
    def processWOA(msg):
        # Build the pipeline, specify part-of-speech processor's batch size
        nlp = stanza.Pipeline(lang = "en", processors = "tokenize,ner") 
        msg1 = nlp(msg)
        ner_workOfArt = [ent.text for ent in msg1.ents if "WORK_OF_ART" in ent.type]

        if len(ner_workOfArt)>0:
            resp =  f"I have heard about {ner_workOfArt[0]}. It is a great work of art!\n" 
            return resp
        resp = ""
        return resp
    @staticmethod
    def processPerson(msg):
        nlp = stanza.Pipeline(lang = "en", processors = "tokenize,ner") 
        interpret = nlp(msg)
        ner_People = [ent.text for ent in interpret.ents if "PERSON" in ent.type]
        return ner_People

