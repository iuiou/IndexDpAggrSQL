import pandas as pd
import numpy as np

customIndex = "Gtestdata/Indexresult/oneDimIndex.csv"
indexWithNoise = "Gtestdata/Indexresult/noisyOneDimIndex.csv"

CI = pd.read_csv(customIndex, header = 0)
IWN = pd.read_csv(indexWithNoise, header = 0)

