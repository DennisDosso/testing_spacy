#!/usr/bin/env python

"""Simple script to test basic spacy functionalities

This works with token and their characteristics.
we show the following information from a simple sentence:

show the following information:
Text: The original word text.
Lemma: The base form of the word.
POS: The simple UPOS part-of-speech tag.
Tag: The detailed part-of-speech tag.
Dep: Syntactic dependency, i.e. the relation between tokens.
Shape: The word shape – capitalization, punctuation, digits.
is alpha: Is the token an alpha character?
is stop: Is the token part of a stop list, i.e. the most common words of the language?

@authors Dennis Dosso
@from https://spacy.io/usage/spacy-101
"""

import spacy

# download in the virtual environment the pre-trained model using:
# python -m spacy download en_core_web_sm

# load the model from disk
nlp = spacy.load("en_core_web_sm")

# immediateli give a document (here a simple string) to the model
# it produces a document containing the informaiton being extracted
doc = nlp("Apple is looking at buying U.K. startup for $1 billion")

for token in doc:
    print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
          token.shape_, token.is_alpha, token.is_stop)
