                                                                                          ###### Example codes
from functools import partial
from multiprocessing import Pool

def print_honorifics(prefix, suffix, samasama, fixed=0):
    print(prefix+'_'+suffix+'_'+samasama+'_'+str(fixed))

partial_print_honorifics = partial(print_honorifics, samasama='SAMASAMA!')
list_of_parameters = [['Mr', 'san'], ['Dr', 'sensei']]
pool=Pool(processes=2)

result = pool.starmap_async(partial_print_honorifics, list_of_parameters)