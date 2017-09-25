import re
import os
import wget
import sys
# import httplib, urllib

if len(sys.argv) != 2:
    print('usage: python piano-midi.py [destination_directory_including_slash]')
    sys.exit()

file_to_parse = open(os.path.join(os.path.dirname(os.getcwd()),"Data", "piano-midi.txt"))

urls = []

for line in file_to_parse:
  url_list = re.findall(r'href=[\'"]?([^\'" >]+)', line)
  if len(url_list) > 0:
    url = url_list[0]
    if 'mp3_link.php?id=' in url:
      url = 'http://www.piano-midi.de/'+url
      urls.append(url)

for url in urls:
  name = url.split('file=')[1]
  file_name = wget.download(url, out=sys.argv[1]+name)
  

  

