A little python project used to learn how to work with scyPy with italian models.

What it includes:

* directory test_scripts: contains simple scripts to play with scipy and see how its basic operations work.
* directory train: contains the training data in a python file (they are JSON at the end of the day)
* direvtory data: contains txt files that can also be used to test the models
* directory test_spacy_italian: contains some scripts to expand/train/test models in italian
    * expand_model.py: adds label to a model, updates it with training data, saves it on disk (be careful with the paths)
    * test_new_model.py and test_original_model.py, used to quickly check the different performances of the two models
    (the original one and the new updated one) on the same strings of text)
    * test_model_with_txt_file.py: like the previous twos, only it loads data from a txt file.


### NB Forgetting phenomenon
It appears that, after the update, the model works worse on some labels. An example of obtained output on the text in
article.txt is the following:
`prima

Franco Battiato PER
Francesco Battiato PER
Riposto LOC
Ionia LOC
provincia di Catania LOC
Liceo Scientifico "Archimede" di Acireale LOC
New York LOC
Roma LOC
Milano LOC

===
dopo

Franco Battiato PER
Francesco Battiato PER
Ionia LOC
Catania ALIMENTO
Liceo Scientifico "Archimede" di LOC
Acireale ALIMENTO
padre ALIMENTO
New York LOC
Roma LOC
Milano LOC`