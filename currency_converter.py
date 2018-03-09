import argparse
import sys
import os.path

def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

def _convert_currency(currency, value):
    """
    This function returns the converted value.
    Note that this function is used internally and should not be called by the user.
    :param currency: multiplier
    :param value: value which should be converted
    :return: new converted value
    """
    return currency * float(value)


def _validate_args():
    """
    This function is used to provide the documentation and validate the arguments
    Note that this function is used internally and should not be called by the user.
    :return: tuple where the first element is the multiplier and the second is the field number
    """
    # Parse arguments and provide usage message
    parser=argparse.ArgumentParser(
        description='''Currency converter''')
    parser.add_argument('field', type=int, help="The column number of the entry "
                                                                        "to be converted.")
    parser.add_argument('multiplier', type=float, help="Conversion rate/Currency exchange rate.")
    parser.add_argument('--header', type=bool, help="False indicates the csv file has no header row.", default=True)
    args=parser.parse_args()

    header = False if args.header is False else True
    # Return Multiplier, field, header
    return args.multiplier, args.field, header


def _convert_line(line, multiplier, field, i):
    """
    This function returns a newline after converting the value in the column number<field>.
    Note that this function is used internally and should not be called by the user.
    Precondition: line is a row of a csv file
    Post-condition: the only changed value in <line> is the <field> column
    :param line: string storing a row of the csv file
    :param multiplier: float storing currency exchange rate
    :param field: int storing the number of the entry that needs to be converted in the row
    :param i: line number in csv file
    :return: string containing the same row with the new converted value
    """
    # Separate the input using the conventional , for the csv files
    inputs = line.split(",")

    # Check for additional commas and chars
    if not is_float(inputs[field - 1]):
        sys.stderr.write("Warning: On line number " + str(i+1) + ", the field number " + str(field) +
                         " is not a float\n")
        return line

    # Convert currency
    inputs[field - 1] = _convert_currency(multiplier, inputs[field - 1])

    # Concatenate the input again into one line and append the network newline character
    new_line = ','.join(map(str, inputs))
    new_line += '\r\n'

    return new_line


def convert(csv_file=None, output_file=None, multiplier=None, field=None, header=True):
    """
    This is the main function which should be called.
    This function calls the other helper functions to convert
    :param csv_file: parameter storing the path to csv file being converted, if the variable is set to an
    existing file, this file is converted. Otherwise, convert reads from stdin
    :param output_file: if this parameter is set, the program writes its output to this path
    """
    if csv_file is None or os.path.isfile(csv_file) is False:
        inputfile = sys.stdin
    else:
        inputfile = open(csv_file, 'r')
    if output_file is None:
        output = sys.stdout
    else:
        output = open(output_file, 'w')
    # If the first line is a header line
    # Read the first_line and write it right after without change since it contains titles
    if header is True:
        first_line = inputfile.readline()
        output.write(first_line)
    # Read the rest of the file
    file = inputfile.read()
    # Separate the lines of the file into a list
    #lines = file.split('\r\n')
    lines = file.splitlines()
    # Go through each line in the file
    for i, line in enumerate(lines):
        # write the new_line to stdout
        new_line = _convert_line(line=line, multiplier=multiplier, field=field, i=i)
        output.write(new_line)


if __name__ == "__main__":
    multiplier, field, header = _validate_args()
    convert(csv_file=None, output_file=None, multiplier=multiplier, field=field, header=True)