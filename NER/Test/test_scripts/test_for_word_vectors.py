import spacy

nlp = spacy.load("en_core_web_md")
tokens = nlp("dog cat banana afskfsd")

# return, for each token, its text, if it has a vector representation
# in the model we loaded, the norm of the vector, if the wrd is out of vocabulary for this model
for token in tokens:
    print(token.text, token.has_vector, token.vector_norm, token.is_oov)
