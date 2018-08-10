from urllib.request import urlopen
from bs4 import BeautifulSoup
from youtube_dl import YoutubeDL

url = "https://www.apple.com/itunes/charts/songs/"
html_content = urlopen(url).read()

soup = BeautifulSoup(html_content, "html.parser")
ul = soup.find("ul", class_=None)
li_list = ul.find_all("li")

options = {
    'default_search': 'ytsearch',
    'format': 'bestaudio/audio'
}
dl = YoutubeDL(options)

for li in li_list:
    name = li.h3.a
    artist = li.h4
    keyword = name.string + " " + artist.string
    dl.download([keyword])