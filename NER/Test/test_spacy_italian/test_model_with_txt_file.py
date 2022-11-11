import spacy

"""Script to test NER using a model and a text file saved on disk"""

# import from spacy the italian model (you need to install it with pip install before using it)
# nlp = spacy.load("it_core_news_lg")  # original model
nlp = spacy.load("../../../model")  # updated model

with open("../data/article.txt") as file:
    # read a small document containing some text in italian
    article = file.read()
    # apply the model to the article
    doc = nlp(article)

    # now, for each recgnized entity in the document...
    for ent in doc.ents:
        # print the recognized text and the label that was associated.
        print(ent.text, ent.label_)
