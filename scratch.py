from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

for i in range(342, 372):
    URL = "https://comic.naver.com/webtoon/detail.nhn?titleId=552960&no=" + str(i) + "&weekday=fri"
    html = urlopen(URL)
    soup = BeautifulSoup(html, 'lxml')

    rawrating = str(soup.find_all('strong'))
    rating = re.search("(\d\.\d\d)", rawrating)
    print(rating.group())
