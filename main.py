import requests as rq
from bs4 import BeautifulSoup
from noti import send

head_title = ["정치","경제","사회","생활/문화","세계","IT/과학"]
url = 'https://news.naver.com/'
req=  rq.get(url)
soup = BeautifulSoup(req.text,"html.parser")

for idx in range(0,6):
    head = head_title[idx]+"\n"
    ranking_titles = soup.select(f"#ranking_10{idx} > ul > li > a")
    body_data = ""
    for idx,rank in enumerate(ranking_titles,1):
        body_data += f'{idx}위 {rank.text}\n-{url+rank["href"]}\n'
    data = head+body_data
    send(data)
