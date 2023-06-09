Naver Korean Audio Scraper
==

Automates bulk downloads of pronounciation audio from the Naver Korean dictionary website. Takes a list of words on the command line or a CSV file.

```
usage: main.py [-h] [--csv-file CSV_FILE] [--csv-delimeter CSV_DELIMETER]
               [--output-folder OUTPUT_FOLDER]
               [korean_words [korean_words ...]]

positional arguments:
  korean_words          Space separated list of korean words to fetch audio samples for (default:     
                        None)

optional arguments:
  -h, --help            show this help message and exit
  --csv-file CSV_FILE   CSV file to source korean words from, if specified will ignore cmdline words  
                        (default: None)
  --csv-delimeter CSV_DELIMETER
                        CSV delimeter separating words (default: ,)
  --output-folder OUTPUT_FOLDER
                        Output path to write .mp3 files to (default: .)
```
