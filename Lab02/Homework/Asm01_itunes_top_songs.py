from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
# download webpage
url = "https://www.apple.com/itunes/charts/songs/"
html_content = urlopen(url).read()
# save webpage to file
# f = open("itunes_top_songs.html", "wb")
# f.write(html_content)
# f.close()
# extract ROI
soup = BeautifulSoup(html_content, "html.parser")
ul = soup.find("ul", class_=None)
li_list = ul.find_all("li")
data = []
for li in li_list:
    entry = {}
    name = li.h3.a
    artist = li.h4.a
    entry["Names"] = name.string    
    entry["Artists"] = artist.string
    data.append(entry)
pyexcel.save_as(records=data, dest_file_name="itunes_top_songs.xlsx")
