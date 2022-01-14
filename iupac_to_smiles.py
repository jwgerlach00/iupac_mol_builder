import rdkit
from rdkit import Chem
import json
import re

iupac = '3-dimethylhexane'

prefix_seperator = ','
number_seperator = '-'


def open_json(filename):
    with open(filename) as file:
        return json.load(file)


prefixes = open_json('prefixes.json')
alkanes = open_json('alkanes.json')

