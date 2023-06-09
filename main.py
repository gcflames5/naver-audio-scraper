import requests
import re
import pdb

word_escaped = requests.utils.quote('환불')
dict_url = f"https://dict.naver.com/search.dict?dicQuery={word_escaped}&query={word_escaped}&target=dic&ie=utf8&query_utf=&isOnlyViewEE="
print(dict_url)

dict_page = requests.get(dict_url)
playlist_match_compiled = re.compile(r'playlist=\"([^ ]*)\"')
matches = playlist_match_compiled.findall(dict_page.text)
audio_url = matches[0]
print(audio_url)
audio_page = requests.get(audio_url)

with open('test.mp3', 'wb') as f:
    f.write(audio_page.content)