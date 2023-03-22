import spacy
nlp = spacy.load("en_core_web_sm")
doc = nlp("He works at Google.")
spacy.displacy.serve(doc, style="ent")
