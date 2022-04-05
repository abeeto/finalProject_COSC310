import stanza

nlp = stanza.Pipeline(lang='en', processors='tokenize,ner')
doc = nlp("What are people tweeting about Elon Musk")
print(*[f'entity: {ent.text}\ttype: {ent.type}' for ent in doc.ents], sep='\n')

doc = nlp("Chris Manning teaches at Stanford University. He lives in the Bay Area.")
print(*[f'entity: {ent.text}\ttype: {ent.type}' for ent in doc.ents], sep='\n')
