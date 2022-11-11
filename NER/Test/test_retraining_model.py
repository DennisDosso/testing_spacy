from doctest import Example

import spacy
import random
from spacy.util import minibatch, compounding
from pathlib import Path
# from spacy import nlp
# from spacy.training import Example

# array containing the new training data for an italian spacy model
from train.training_data import TRAIN_DATA

# import the italian model
nlp = spacy.load("it_core_news_lg")

ner = nlp.get_pipe("ner")

# we add the new labels
for _, annotations in TRAIN_DATA:
    for ent in annotations.get("entities"):
        ner.add_label(ent[2])

# get names of other pipes to disable them dring training
pipe_exceptions = ["ner", "trf_wordpiecer", "trf_tok2vec"]
other_pipes = [pipe for pipe in nlp.pipe_names if pipe not in pipe_exceptions]

# let us use 20 iterations to traing the model
n_iter = 20

# disable them
with nlp.disable_pipes(*other_pipes):  # only train NER
    examples = []
    optimizer = nlp.resume_training()
    for text, annots in TRAIN_DATA:
        examples.append(Example.from_dict(nlp.make_doc(text), annots))
    for itn in range(n_iter):
        random.shuffle(examples)
        losses = {}
        for batch in minibatch(examples, size=compounding(4.0, 16.0, 1.001)):
            nlp.update(batch, sgd=optimizer, drop=0.2, losses=losses)
        print('losses : ', losses)
