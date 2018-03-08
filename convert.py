import argparse
import sys

def convert_currency(currency, value):
    """
    This function returns the converted value.
    This function is made so it is able to convert values back and forth with no hard coding.
    :param currency: multiplier
    :param value: value which should be converted
    :return: new converted value
    """
    if value < 0:
        return currency
    return currency * float(value)

parser=argparse.ArgumentParser(
    description='''Currency converter''')
parser.add_argument('--field', type=int)
parser.add_argument('--multiplier', type=float)
args=parser.parse_args()
multiplier = args.multiplier
field = args.field
first_line = sys.stdin.readline()
sys.stdout.write(first_line)
file = sys.stdin.read()
lines = file.split("\r\n")
for line in lines:
    inputs = line.split(",")
    inputs[field - 1] = convert_currency(multiplier, inputs[field - 1])
    new_line = ','.join(map(str, inputs))
    new_line += "\r\n"
    line = new_line
    sys.stdout.write(line)