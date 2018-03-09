# Currency Converter

This program converts the currency used in a csv file. The entry number is determined by the field variable
and the exchange rate is determined by the multiplier variable when running the program through the command line.

## Getting Started

**Open up the terminal on your computer and run the following commands sequentially:**

**git clone https://github.com/amrrsharaff/CodingAssignment.git**


**cd CodingAssignment**


**python currency_converter.py -field [field number] -multiplier [rate] (--header False) < [PATH TO SOURCE] > [PATH TO NEW]**

The last command can be also run using input and output optional arguments as follows:

**python currency_converter.py -field [field number] -multiplier [rate] (--header False) -i [PATH TO SOURCE] -o [PATH TO NEW]**


### Prerequisites

**In order to run the program, you need:**
- Python 2.7 
(To install, follow the guidelines on https://www.python.org/download/releases/2.7/)
- ArgParse library
(To install, open the command line and run)
- **pip install argparse**

## Running the tests

To run the tests for the program, open the terminal and navigate to the CodingAssignment folder and run:
- **python currency_converter.py -field 3 -multiplier 2 < test1.py > test1out.py**

or

- **python currency_converter.py -field 3 -multiplier 2 -i test1.py -o test1out.py**

You should be able to have a warning for non float entry, to confirm this warning, you can open the csv file called "test1.csv" and look at the entry which should be converted.

## Deployment

This program can be easily integrated into other apps by importing the module and calling the function convert.

## Built With

* [Python 2.7](https://www.python.org/download/releases/2.7)

## Notes:
- The program gives you a warning and does not cause any change for every line which:
- (1) does not have the right number of entries
- (2) has the field which should be converted as a non-numeric value.
- The program leaves anything but the value being converted unchanged.
- test2.csv is made for unit testing and can be used instead of test1 as above.

## Authors

Amr Sharaf
