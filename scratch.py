from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker



data=[]
for i in range(342, 372):
    URL = "https://comic.naver.com/webtoon/detail.nhn?titleId=552960&no=" + str(i) + "&weekday=fri"
    html = urlopen(URL)
    soup = BeautifulSoup(html, 'lxml')

    rawrating = str(soup.find_all('strong'))
    rating = re.search("(\d\.\d\d)", rawrating)
    pp=rating.group()

    print('Rating : ' ,pp)
    data.append(pp)

#print(data)

x = [342,343,344,345,346,347,348,349,350,351,352,353,354,355,356,357,358,359,360,361,362,363,364,365,366,367,368,369,370,371]
y = data
plt.figure(figsize=(30,5))
plt.xlabel('webtoon episode')
plt.ylabel('Rating')
plt.title('Changes in ratings of webtoons')
ax=plt.axes()
ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
plt.plot(x,y,'g')
plt.xlim(342,371)
plt.ylim(4,10)
plt.show()
