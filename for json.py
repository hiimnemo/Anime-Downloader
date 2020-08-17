"""
OK GUYS... I HAVE made the best anime downloader fully automated as bes t as possible.
requirements:
1. pip3 youtube-dl
2. pip3 requests
3. pip3 bs4

if the video doesnt download something is wrong with crunchy and IT IS NOT MY FAULT..i have even included the fking try and except shit.
i personally dont like it, idk why.

so good luck and hf :)



"""




from urllib.request import urlopen, urlretrieve
import requests
from bs4 import BeautifulSoup
import time
import json

input("PLEASE TYPE in \"Mallu is a fking idiot\" as is to proceed further: ")

url = input("Please type in the complete URL from anibd.net: ")
url = str(url)

headers = { 
    "Accept-Language" : "en-US,en;q=0.5",
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0"

}

r = requests.get(url, headers=headers)
bs = BeautifulSoup(r.content, 'html.parser')

options = bs.find_all('a', {"class" :"i_icon i_resource_crunchyroll", "data-anidb-rel": "anidb::extern", "title" : "watch on crunchyroll"})
options_2 = bs.find_all("td", {"class": "title name episode"})

print(len(options), len(options_2))
url_one = []
name = []
for i in range(0, len(options)):
    url_one = url_one + [options[i]]
for i in range(0, len(options_2)):
    name = name + [options_2[i]]


dic_to_be_written = {}
for i in range(0, len(options)): #len(options)
    
    dictionary = {str(i+1): { 'Episode Name': str(name[i])[str(name[i]).find(">", str(name[i]).find("<label itempr"))+1:str(name[i]).find("</label")].strip(), 'URL': str(url_one[i])[str(url_one[i]).find("href")+6:str(url_one[i]).find("title")-2].strip()}}
    print(dictionary )
    dic_to_be_written = {**dic_to_be_written, **dictionary }


json_dumps = json.dumps(dic_to_be_written, indent= 4)

name_of_the_file = input("what do u want to name the file as? ")

with open(name_of_the_file+".json", 'a') as f :
    f.write(json_dumps)


 