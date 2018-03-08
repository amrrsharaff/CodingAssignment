import argparse
import sys


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
    parser.add_argument('--field', type=int, required=True, description="The column number of the entry "
                                                                        "to be converted.")
    parser.add_argument('--multiplier', type=float, required=True, description="Conversion rate/Currency exchange rate.")
    parser.add_argument('--header', type=bool, description="False indicates the csv file has no header row.")
    args=parser.parse_args()

    header = False if args.header is False else True
    # Return Multiplier, field
    return args.multiplier, args.field, header


def _convert_line(line, multiplier, field):
    """
    This function returns a newline after changing the value in the field <field>.
    Note that this function is used internally and should not be called by the user.
    Precondition: line is a row of a csv file
    Post-condition: the only changed value in <line> is the <field> column
    :param line: string storing a row of the csv file
    :param multiplier: float storing currency exchange rate
    :param field: int storing the number of the entry that needs to be converted in the row
    :return: string containing the same row with the new converted value
    """
    # Separate the input using the conventional , for the csv files
    inputs = line.split(",")

    # Convert currency
    inputs[field - 1] = _convert_currency(multiplier, inputs[field - 1])

    # Concatenate the input again into one line and append the network newline character
    new_line = ','.join(map(str, inputs))
    new_line += "\r\n"

    return new_line


def convert():
    """
    This is the main function which should be called.
    This function calls the other helper functions to convert
    """
    multiplier, field, header = _validate_args()
    # If the first line is a header line
    # Read the first_line and write it right after without change since it contains titles
    if header is True:
        first_line = sys.stdin.readline()
        sys.stdout.write(first_line)
    # Read the rest of the file
    file = sys.stdin.read()
    # Separate the lines of the file into a list
    lines = file.split("\r\n")
    # Go through each line in the file
    for line in lines:
        # write the new_line to stdout
        new_line = _convert_line(line=line, multiplier=multiplier, field=field)
        sys.stdout.write(new_line)

if __name__ == "__main__":
    convert()