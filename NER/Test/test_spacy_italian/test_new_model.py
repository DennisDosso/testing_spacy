"""Script to test the new italian model with a new label. First run test_retraining_model

"""

import spacy

print("Load the new model from disk")
model_dir = "../../../model"
nlp = spacy.load(model_dir)

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
