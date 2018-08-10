from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
url = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"
html_content = urlopen(url).read()

f = open("VNM_baocaotaichinh.html", "wb")
f.write(html_content)
f.close()

soup = BeautifulSoup(html_content, "html.parser")
excel_data = []

div_r = soup.find("div", {"id" : "divTableHeader"})
td_list = div_r.table.tr.find_all("td", "h_t")
div_c = soup.find("div", {"style": "overflow:hidden;width:100%;border-bottom:solid 1px #cecece;"})
table = div_c.find("table")
tr_list = table.find_all("tr")

for td in td_list:
    coll_name = td.string
    print(coll_name)


for tr in tr_list:
        td_content_list = tr.find("td", {"class": "b_r_c"})
        if td_content_list != None:
            for td_content in td_content_list:
                print(td_content.string)
        td_data_list = tr.find_all("td", {"align": "right"})
        for td_data in td_data_list:
            if td_data != None:
                print(td_data.string)

# gâu gâu khó quá baiz