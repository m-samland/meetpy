print('# ~ Nessie')

def nessie(*args, **kwargs):
    """
    Generates a nessie from your input parameters.

    Args for Constructor:
        name:           name of your creature
        color:          color of your nessie (mandatory)
                        available colors are:
                            - grey
                            - red
                            - green
                            - yellow
                            - blue
                            - magenta
                            - cyan
                            - white
        length:         something between 1-3, default is: random length

    properties:
        self. color     color of your nessie
        self.length     length of nessie
    """

    return __Nessie__(*args, **kwargs)


class __Nessie__(object):
    """
    Nessie object.
    'Better use a class, so it knows where it goes!'

    Properties:
        name:           name of your creature
        color:          color or your nessie
        length:         length of your nessie

    Methods:
        say_hi:         nessie just wanna play
    """

    def __init__(self, name, color='green', length=False):
        import random

        allowedLength = [1,2,3]

        self.name = name
        self.color = color

        if length != False and type(length) == type(123) and length in allowedLength:
            self.length = length
        else:
            self.length = random.choice(allowedLength)


    def say_hi(self):
        from ..backpack.termcolor import colored

        if self.length == 1:
            print(colored('                     Hi, Im '+self.name+'!', self.color))
            print(colored("              _a_a", self.color))
            print(colored("             {/ ''\_", self.color))
            print(colored("        _   {|  ._oo)", self.color))
            print(colored("       { \  {/  |", self.color))
            print(colored("~^~^~`~^~`~^~^~^~`^~~", self.color))

        elif self.length == 2:
            print(colored('                                     Hi, Im '+self.name+'!', self.color))
            print(colored("                _   _       _a_a", self.color))
            print(colored("              _{.`=`.}_    {/ ''\_", self.color))
            print(colored("        _    {.'  _  '.}  {|  ._oo)", self.color))
            print(colored("       { \  {/  .' '.  \} {/  |", self.color))
            print(colored("~^~^~`~^~`~^~`^~^~`^~^~^~^~^~^~`^~~", self.color))

        elif self.length == 3:
            print(colored('                                               Hi, Im '+self.name+'!', self.color))
            print(colored("                          _   _       _a_a", self.color))
            print(colored("              _   _     _{.`=`.}_    {/ ''\_", self.color))
            print(colored("        _    {.`'`.}   {.'  _  '.}  {|  ._oo)", self.color))
            print(colored("       { \  {/ .-. \} {/  .' '.  \} {/  |", self.color))
            print(colored("~^~^~`~^~`~^~`~^~`~^~^~`^~^~`^~^~^~^~^~^~`^~~", self.color))

        else:
            print('! YOU CREATED A MONSTER!!')

    def debug(self):
        from ..backpack.debug_breakpoint import debug_breakpoint
        debug_breakpoint()
