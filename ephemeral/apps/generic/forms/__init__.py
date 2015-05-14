import os
# -*- coding: utf-8 -*-

to_the_end = []
for module in os.listdir(os.path.dirname(__file__)):
    if module == '__init__.py' or module[-3:] != '.py':
        continue
    try:
        exec('from '+module[:-3]+' import *')
    except:
        to_the_end.append(module[:-3])
for the_end in to_the_end:
   exec('from '+the_end+' import *')
try:
    del module, to_the_end, the_end
except:
    pass
