from selenium import webdriver
import pandas as pd

URL = 'https://kr.investing.com/crypto/bitcoin/historical-data'
chromedriver = 'C:/Users/Park Subin/Desktop/가마우지/chromedriver.exe'

driver = webdriver.Chrome(chromedriver)
driver.get(URL)

l = []

for i in range(30):
    i += 1
    i = str(i)
    date = driver.find_element_by_xpath("/html/body/div[5]/section/div[7]/div[3]/table[1]/tbody/tr["+i+"]/td[1]")
    startday = driver.find_element_by_xpath("/html/body/div[5]/section/div[7]/div[3]/table[1]/tbody/tr["+i+"]/td[2]")
    endday = driver.find_element_by_xpath("/html/body/div[5]/section/div[7]/div[3]/table[1]/tbody/tr["+i+"]/td[3]")
    high = driver.find_element_by_xpath("/html/body/div[5]/section/div[7]/div[3]/table[1]/tbody/tr["+i+"]/td[4]")
    low = driver.find_element_by_xpath("/html/body/div[5]/section/div[7]/div[3]/table[1]/tbody/tr["+i+"]/td[5]")
    amount = driver.find_element_by_xpath("/html/body/div[5]/section/div[7]/div[3]/table[1]/tbody/tr["+i+"]/td[6]")
    percent = driver.find_element_by_xpath("/html/body/div[5]/section/div[7]/div[3]/table[1]/tbody/tr["+i+"]/td[7]")
    l.append([date.text, startday.text, endday.text, high.text, low.text, amount.text, percent.text])

df = pd.DataFrame(l, columns=['날짜', '종가', '오픈', '고가', '저가', '거래량', '변동'])
dff=df.replace(',','')
dff.to_csv('bitt.csv', index=False, encoding='cp949')


driver.quit()