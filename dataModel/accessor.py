import pandas as pd
import json
from dataModel.model import table

class Csvaccessor:
    def __init__(self, config):
        self.configUrl = config
        self.config = None

    def generate(self, root):
        raw_data = pd.read_csv(root, header=0)
        with open(self.configUrl, 'r') as f:
            self.config = json.load(f)
        schema = self.config["attrConfig"]
        return table(self.config["tableName"], schema, raw_data)




