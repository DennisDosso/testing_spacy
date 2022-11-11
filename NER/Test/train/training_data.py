# here we have an array of tuples. Each tuple is composed by a string representing the sentence to learn. THe second part of the tuple
# represents the entities, defined by arrays that identify the starting and ending position and the label that we are applying to it.
# in this case, we are describing elements of the class "ALIMENTO"

TRAIN_DATA = [
    ("Prima di tutto dividete i tuorli dagli albumi e metteteli in due ciotole diverse.",
     {"entities": [(27, 33, "ALIMENTO"), (40, 46, "ALIMENTO")]}),
    ("Unite un cucchiaio di zucchero", {"entities": [(22, 30, "ALIMENTO")]}),
    ("unire il mascarpone", {"entities": [(9, 19, "ALIMENTO")]}),
    ("mescolare le uova", {"entities": [(13, 17, "ALIMENTO")]}),
    ("ricopritela con uno strato di savoiardi imbevuti nella bagna", {"entities": [(30, 39, "ALIMENTO")]}),
    ("Mescolate con il liquore al caffè", {"entities": [(18, 25, "ALIMENTO"), (29, 34, "ALIMENTO")]}),
    ("Usare lo sbattitore", {"entities": []}),
    ("Mangiare la pizza una volta a settimana è d’obbligo", {"entities": [(12, 17, "ALIMENTO")]}),
    ("Ho comprato del latte.", {"entities": [(17, 22, "ALIMENTO")]}),
    ("Marco adora la cioccolata.", {"entities": [(16, 26, "ALIMENTO")]}),
    ("Io e mio cugino andiamo matti per le lasagne.", {"entities": [(38, 45, "ALIMENTO")]}), (
        "Per preparare la pasta, è sufficiente mettere una pentola d’acqua sul fuoco…",
        {"entities": [(18, 23, "ALIMENTO"), (61, 66, "ALIMENTO")]}),
    ("Per preparare il tiramisù, hai bisogno di…", {"entities": [(18, 26, "ALIMENTO")]}), (
        "I savoiardi dovranno essere imbevuti di caffè e poi adagiati in una pirofila.",
        {"entities": [(3, 12, "ALIMENTO")]}),
    ("Il gelato alla nocciola è il mio preferito.", {"entities": [(4, 10, "ALIMENTO"), (16, 24, "ALIMENTO")]}),
    ("Hai mai assaggiato le lasagne al pesto?", {"entities": [(23, 30, "ALIMENTO"), (34, 39, "ALIMENTO")]}),
    ("Per cena cucinerò della pasta.", {"entities": [(20, 25, "ALIMENTO")]}),
    ("Non mi va di cucinare stasera. Ordiniamo della pizza?", {"entities": [(47, 53, "ALIMENTO")]})]
