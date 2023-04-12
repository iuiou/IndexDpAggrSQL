import pandas as pd
import json
from model import table

class Csvaccessor:
    def __init__(self, root, config):
        self.raw_data = pd.read_csv(root, header=0)
        self.configUrl = config
        self.config = None

    def generate(self):
        with open(self.configUrl, 'r') as f:
            self.config = json.load(f)
        schema = self.config["attrConfig"]
        return table(self.config["tableName"], schema, self.raw_data)


