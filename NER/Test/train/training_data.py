# here we have an array of tuples. Each tuple is composed by a string representing the sentence to learn. THe second part of the tuple
# represents the entities, defined by arrays that identify the starting and ending position and the label that we are applying to it.
# in this case, we are describing elements of the class "ALIMENTO"

TRAIN_DATA = [
    ("Prima di tutto dividete i tuorli dagli albumi e metteteli in due ciotole diverse.",
     {"entities": [(26, 32, "ALIMENTO"), (39, 45, "ALIMENTO")]}),
    ("Unite un cucchiaio di zucchero", {"entities": [(22, 30, "ALIMENTO")]}),
    ("unire il mascarpone", {"entities": [(9, 19, "ALIMENTO")]}),
    ("mescolare le uova", {"entities": [(13, 17, "ALIMENTO")]}),
    ("ricopritela con uno strato di savoiardi imbevuti nella bagna", {"entities": [(30, 39, "ALIMENTO")]}),
    ("Mescolate con il liquore al caffè", {"entities": [(17, 24, "ALIMENTO"), (28, 33, "ALIMENTO")]}),
    ("Usare lo sbattitore", {"entities": []}),
    ("Mangiare la pizza una volta a settimana è d’obbligo", {"entities": [(12, 17, "ALIMENTO")]}),
    ("Ho comprato del latte.", {"entities": [(16, 21, "ALIMENTO")]}),
    ("Marco adora la cioccolata.", {"entities": [(15, 25, "ALIMENTO")]}),
    ("Io e mio cugino andiamo matti per le lasagne.", {"entities": [(37, 44, "ALIMENTO")]}), (
        "Per preparare la pasta, è sufficiente mettere una pentola d’acqua sul fuoco…",
        {"entities": [(17, 22, "ALIMENTO"), (60, 65, "ALIMENTO")]}),
    ("Per preparare il tiramisù, hai bisogno di…", {"entities": [(17, 25, "ALIMENTO")]}), (
        "I savoiardi dovranno essere imbevuti di caffè e poi adagiati in una pirofila.",
        {"entities": [(2, 11, "ALIMENTO")]}),
    ("Il gelato alla nocciola è il mio preferito.", {"entities": [(3, 9, "ALIMENTO"), (15, 23, "ALIMENTO")]}),
    ("Hai mai assaggiato le lasagne al pesto?", {"entities": [(22, 29, "ALIMENTO"), (33, 38, "ALIMENTO")]}),
    ("Per cena cucinerò della pasta.", {"entities": [(24, 29, "ALIMENTO")]}),
    ("Non mi va di cucinare stasera. Ordiniamo della pizza?", {"entities": [(47, 52, "ALIMENTO")]})]
