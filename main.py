import argparse 
import requests
import re
import pdb
import logging

import naver_dict as nd

class ArgParser(argparse.ArgumentParser):
    '''
    Wrapper module to parse command line
    '''

    def __init__(self):
        super().__init__(formatter_class=argparse.ArgumentDefaultsHelpFormatter)

        # List of words on the command line
        self.add_argument("korean_words",
                          nargs="*",
                          help="Space separated list of korean words to fetch audio samples for")

        # Optional CSV Arguments
        self.add_argument("--csv-file",
                          type=str,
                          help="CSV file to source korean words from, if specified will ignore cmdline words")

        self.add_argument("--csv-delimter",
                          type=str, default=",",
                          help="CSV delimeter separating words")
        self.add_argument("--output-folder",
                          type=str, default=".",
                          help="Output path to write .mp3 files to")

def config_logger():
    logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def main():
    config_logger()

    arg_parser = ArgParser()
    args = arg_parser.parse_args()

    word_list = []

    if len(args.korean_words) > 0:
        word_list = args.korean_words

    naver_dict = nd.NaverDict()
    naver_dict.bulk_fetch(word_list, args.output_folder)

if __name__ == "__main__":
    main()
