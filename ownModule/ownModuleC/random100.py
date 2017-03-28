
def random100():
    """ Returns some form a 100.

    Beware! I did not name this one random, since random is an already existing
    module! With newst version of python3 one specially has to state where the
    function/object/module is that one whats to import, e.g. via '.' .
    """
    import random

    foo = [100, '100', 100.000, {'100': 100}, 'hundred', 'hundert']

    return random.choice(foo)
