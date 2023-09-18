import os
import re
import requests
import logging

class NaverDict():
    '''
    Utilities for the Naver dictionary
    '''
 
    def fetch_audio_file(self, word, output_folder):
        # Build the rest of the url
        headers = {
            'authority': 'dict.naver.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'range': 'bytes=0-',
            'referer': 'https://dict.naver.com/dict.search?query=%EB%AC%B8',
            'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'audio',
            'sec-fetch-mode': 'no-cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
        }

        params = {
            'service': 'dictionary',
            'speech_fmt': 'mp3',
            'speaker': 'mijin',
            'text': word,
        }

        response = requests.get('https://dict.naver.com/api/nvoice', params=params, headers=headers)

        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
            
        with open(os.path.join(output_folder, f'{word}.mp3'), 'wb') as f:
            f.write(response.content)

    def bulk_fetch(self, words, output_folder):
        for word in words:
            logging.info(f"Fetching audio for {word}...")
            try:
                self.fetch_audio_file(word, output_folder)
            except Exception:
                logging.error(f"Failed to fetch audio for {word}")

