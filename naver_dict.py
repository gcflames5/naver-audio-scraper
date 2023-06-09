import os
import re
import requests
import logging

class NaverDict():
    '''
    Utilities for the Naver dictionary
    '''
    def __init__(self):
 
        self.base_url = 'https://dict.naver.com/search.dict?target=dic&ie=utf8&query_utf=&isOnlyViewEE=' # dictionary url
        self.playlist_regex = re.compile(r'playlist=\"([^ ]*)\"') # regex of the first audio clip
 
    def fetch_audio_file(self, word, output_folder):
        # Build the rest of the url
        word_escaped = requests.utils.quote(word)
        dict_url = f'{self.base_url}&dicQuery={word_escaped}&query={word_escaped}'

        # Fetch the dictionary page & parse playlists
        dict_page = requests.get(dict_url)
        playlist_matches = self.playlist_regex.findall(dict_page.text)

        if playlist_matches == None or len(playlist_matches) < 1:
            raise Exception(f'Saw no playlist_matches for {word}! URL: {dict_url}')

        # Grab the audio and write it to a file
        audio_page = requests.get(playlist_matches[0])

        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
            
        with open(os.path.join(output_folder, f'{word}.mp3'), 'wb') as f:
            f.write(audio_page.content)

    def bulk_fetch(self, words, output_folder):
        for word in words:
            logging.info(f"Fetching audio for {word}...")
            try:
                self.fetch_audio_file(word, output_folder)
            except Exception:
                logging.error(f"Failed to fetch audio for {word}")

