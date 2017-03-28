""" ownModule - Doc
This module provides you with the full power of the number 100
and can host different monsters.

Monsters implemented:
    - nessie

Access 100 via ownModuleD.variable.
Try the help function.

Sub-modules: none
"""
print('Hey there!')

variable = 100

def help():
    print('# ownModule Version B \n - nothing but full 100')
    print('# Do you really need help? Try .variable')

from .random100 import random100
from .messy import nessie
#from .__not_messy__ import ok
