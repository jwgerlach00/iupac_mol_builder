import re

formula = 'C3H8'

# Find all numbers
number = {}
index = {}
for match in re.finditer('[0-9]+', formula):
    i = match.start()
    num = int(match.group())
    atom = formula[i - 1]
    
    number[atom] = num
    index[atom] = i

alkane = True if len(number.keys()) == 2 and 'C' in ''.join(number.keys()) and 'H'

diff_atoms = len(number.keys())