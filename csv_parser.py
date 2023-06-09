import csv

class CSVParser:
    '''
    Utilities for reading CSV files
    '''

    def parse_word_list(self, csv_file, delim):
        word_list = []

        with open(csv_file, newline='', encoding="utf8") as f:
            csv_reader = csv.reader(f, delimiter=delim)
            for row in csv_reader:
                for entry in row:
                    word_list.append(entry)

        return word_list