import json
import youtube_dl

name_of_the_file = input("Pls type in the name of the file(excluding the extenstion): ")

with open(name_of_the_file+".json") as f:
  data = json.load(f)


for i in range(0, len(data)):
    print(str(i+1) +" ." + data[str(i+1)]['Episode Name'])
input_1 = input("From which episode do u want it to be downloaded? ")
input_2 = input("Till what episode do u want? ")

URLs = []
for i in range(int(input_1)-1, int(input_2)):
    URLs = URLs + [data[str(i+1)]['URL']]

print(URLs)

print("Assuming that the formats are same for each episode, i will ask for one episode")

try:
    ydl_opts = {} 
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(str(URLs[0]), download=False)



    print("the available formats are: \n")
    Formats = {}
    Formats_not_displayed = {}
    for i in range(len(info['formats'])):
        dic__ = {str(i):str(info['formats'][i]['format'])}
        dic_not_displayed = {str(i):str(info['formats'][i]['format_id'])}
        Formats = {**Formats, **dic__}
        Formats_not_displayed = {**Formats_not_displayed, **dic_not_displayed}

    json_dumps = json.dumps(Formats, indent=2)    
    print(json_dumps)

    format__1 = str(input("Type in the number :"))

    format__2 = Formats_not_displayed[str(format__1)]

    print("DOWNLOADING WITH THIS " + str(format__2))

    ydl_opts = {'format': str(format__2)}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(URLs)

except:
    ydl_opts = {'format': 'Best'}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(URLs)



