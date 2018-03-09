import argparse
import sys
import os.path

def is_float(string):
    """
    This function checks if string can be converted to a float
    :param string: a string which is expected to be a float
    :return: True if string is a float and False if it's not.
    """
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
    :return: tuple containing the command line arguments
    """
    # Parse arguments and provide usage message
    parser=argparse.ArgumentParser(
        description='''Currency converter''')
    parser.add_argument('-field', type=int, required=True, help="The column number of the "
                                                                "entry to be converted. (Required)")
    parser.add_argument('-multiplier', type=float, required=True, help="Conversion rate/"
                                                                       "Currency exchange rate. (Required)")
    parser.add_argument('--header', type=bool, help="False indicates the csv file has no header row.", default=True)
    parser.add_argument('-i', type=str, help="Input csv file", default=None)
    parser.add_argument('-o', type=str, help="Output csv file", default=None)
    args=parser.parse_args()

    header = False if args.header is False else True
    # Return Multiplier, field, header
    return args.multiplier, args.field, header, args.i, args.o


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
    :param multiplier: exchange rate
    :param field: column number of value being converted
    :param header: true if the first row is a header row and false if it is not
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
    lines = file.splitlines()

    # Go through each line in the file
    for i, line in enumerate(lines):
        # Check if there are as many columns as there should be
        # Rewrite the line if there is a conflict in the number of columns and go to next line
        if len(line.split(",")) < field:
            sys.stderr("Warning: On line number " + str(i + 1) + " the column number "
                                                                 "is more than the number of columns.")
            output.write(line)
            continue

        # write the new_line to stdout
        new_line = _convert_line(line=line, multiplier=multiplier, field=field, i=i)
        output.write(new_line)


if __name__ == "__main__":
    multiplier, field, header, input_file, output_file = _validate_args()
    convert(csv_file=input_file, output_file=output_file, multiplier=multiplier, field=field, header=True)
