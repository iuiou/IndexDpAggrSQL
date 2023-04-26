import random

import pandas as pd
import numpy as np
from dataModel.accessor import Csvaccessor

configdir = '../Gtestdata/DataConfig.json'
datadir = '../Gtestdata/data/'
joinnum = 3
sc = Csvaccessor(configdir)
for i in range(joinnum):
    id = i + 1
    table = sc.generate(datadir + 'testdatafor' + str(id) + '.csv')
    table.create_SegmentT_index('d', 'Sum', 0.1, 'Index/indexfor' + str(id) + '.csv')

print('build allSegmentT index finished!')




