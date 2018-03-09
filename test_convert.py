import unittest
import currency_converter
import sys


class MyTestCase(unittest.TestCase):

    def test_file(self):
        #file = generate_csv_file("test1.csv", "First Name,Last Name,Assets\rAmr,Sharaf,123\rAmr,Toronto,123\r\n")
        currency_converter.convert("test2.csv", "test2out.csv", 2, 3, True)
        output = open("test2out.csv", 'r')
        lines = output.read().splitlines()[1:]
        for line in lines:
            entries = line.split(",")
            self.assertTrue(float(entries[2]), float(entries[2]) * 2)


def generate_csv_file(name, data):
    new_file = open(name, 'a')
    lines = data
    new_file.write(lines)
    return new_file


if __name__ == '__main__':
    unittest.main()
