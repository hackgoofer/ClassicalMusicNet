import re
import os
import wget

file_to_parse = open(os.path.join(os.path.dirname(os.getcwd()),"Data", "amclassical.txt"))

urls = []

for line in file_to_parse:
  url_list = re.findall(r'href=[\'"]?([^\'" >]+)', line)
  url = 'http://www.amclassical.com'+url_list[0]
  urls.append(url)

for url in urls:
  name = url.split('/mp3/amclassical_')[1]
  name = name.split('.mp3')[0]
  file_name = wget.download(url)
  

  

