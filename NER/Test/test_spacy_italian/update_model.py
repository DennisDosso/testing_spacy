# from doctest import Example
import spacy
import random
from spacy.util import minibatch, compounding
from pathlib import Path
from spacy.training import Example

"""Add new label to model. Expand it with training examples. Save it on disk."""

# array containing the new training data for an italian spacy model
from NER.Test.train.training_data import TRAIN_DATA

# import the model
nlp = spacy.load("it_core_news_lg")
# extract the element NER of the pipeline - object EntityRecognizer
ner = nlp.get_pipe("ner")

# we add all the labels that are present in the TRAIN_DATA. Duplicate labels are not a problem
for _, annotations in TRAIN_DATA:
    for ent in annotations.get("entities"):
        ner.add_label(ent[2])

# this is the list of steps of the pipeline we DO NOT want to involve in the retraining
unaffected_pipes = ["ner"]
# we populate this list with the OTHER steps of the pipeline
other_pipes = [pipe for pipe in nlp.pipe_names if pipe not in unaffected_pipes]

# let us use 20 iterations to train the model
n_iter = 20

with nlp.disable_pipes(*other_pipes):
    for iteration in range(30):
        random.shuffle(TRAIN_DATA)
        losses = {}
        batches = minibatch(TRAIN_DATA, size=compounding(4.0, 32.0, 1.001))
        for batch in spacy.util.minibatch(TRAIN_DATA, size=2):
            for text, annotations in batch:
                # Create the Example object
                doc = nlp.make_doc(text)
                example = Example.from_dict(doc, annotations)
                # Update model
                nlp.update([example], losses=losses, drop=0.3)
                print("Losses", losses)

# save the model on disk
output_dir = Path("../../../model")
nlp.to_disk(output_dir)
print("New model saved in directory", output_dir)

# code coming from another tutorial, should be similar

# disable them
# with nlp.disable_pipes(*other_pipes):  # only train NER
#     examples = []
#     optimizer = nlp.resume_training()
#     for text, annots in TRAIN_DATA:
#         examples.append(Example.from_dict(nlp.make_doc(text), annots))
#     for itn in range(n_iter):
#         random.shuffle(examples)
#         losses = {}
#         for batch in minibatch(examples, size=compounding(4.0, 16.0, 1.001)):
#             nlp.update(batch, sgd=optimizer, drop=0.2, losses=losses)
#         print('losses : ', losses)
