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

#Parse arguments and provide usage message
parser=argparse.ArgumentParser(
    description='''Currency converter''')
parser.add_argument('--field', type=int)
parser.add_argument('--multiplier', type=float)
args=parser.parse_args()
#Extract multiplier argument
multiplier = args.multiplier
#Extract field argument
field = args.field
#Read the first_line and write it right after without change since it contains titles
first_line = sys.stdin.readline()
sys.stdout.write(first_line)
#Read the rest of the file
file = sys.stdin.read()
#Separate the lines of the file into a list
lines = file.split("\r\n")
#Go through each line in the file
for line in lines:
    #Separate the input using the conventional , for the csv files
    inputs = line.split(",")
    #Convert currency
    inputs[field - 1] = convert_currency(multiplier, inputs[field - 1])
    #Concatenate the input again into one line and append the network newline character
    new_line = ','.join(map(str, inputs))
    new_line += "\r\n"
    line = new_line
    #write the new_line to stdout
    sys.stdout.write(line)