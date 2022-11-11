""" A little script used to test the original italian model

We use this script to compare the NER performances of the original italian model
with the model with a new label added
"""

import spacy

nlp = spacy.load("it_core_news_lg")

# a small test document
doc = "Amo il tiramisù con i savoiardi e la stracciatella"
doc = nlp(doc)
print("Entità:", [(ent.text, ent.label_) for ent in doc.ents])

doc = nlp("Per preparare le tagliatelle, ci vuole la farina")
print("Entità:", [(ent.text, ent.label_) for ent in doc.ents])

doc = nlp("Marco adora la marmellata")
print("Entità:", [(ent.text, ent.label_) for ent in doc.ents])

doc = nlp("Domani andremo a Roma a vedere il Papa")
print("Entità:", [(ent.text, ent.label_) for ent in doc.ents])
