""" Monsters - Documentation
This module provides you with different monsters.

Monsters implemented:
    - nessie, living in loch
"""
print('   _____                           __                    _____                  __     ')
print('  /     \   ____   ____    _______/  |_  ___________    /     \  _____    _____|  |__  ')
print(' /  \ /  \ /  _ \ /    \  /  ___/\   __\/ __ \_  __ \  /  \ /  \ \__  \  /  ___/  |  \  ')
print('/    Y    (  <_> )   |  \ \___ \  |  | \  ___/|  | \/ /    Y    \ / __ \_\___ \|   Y  \ ')
print('\____|__  /\____/|___|  / ____  > |__|  \___  >__|    \____|__   (____  /____  >___|  /')
print('        \/            \/      \/            \/                \/      \/     \/     \/ ')

def help():
    print('# He did the monster mash')
    print('# The monster mash ')
    print('# It was a graveyard smash ')

from . import backpack

print('### Available Monsters ###')
from . import loch


# Some more functions
#def store(monster, path='.monst'):
#    from .backpack import dill_save
#
#    name = monster.name
#    dill_save(monster, name, path)
#    return True
#
#def get(name, path='.monst'):
#    from .backpack import dill_load
#
#    return dill_load(name, path)
