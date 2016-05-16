#登录河海大学信息门户进入登录后页面
import requests
from bs4 import BeautifulSoup

url = "http://my.hhu.edu.cn/"
log_in_url = "http://my.hhu.edu.cn/index.portal"
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36",
    "Cookie":"saveCookie=false; amlbcookie=01; iPlanetDirectoryPro=AQIC5wM2LY4Sfcxq%2FO%2BHpMdFoooTVhzHP6PjD9ZnwoN8FZw%3D%40AAJTSQACMDE%3D%23; JSESSIONID=0000_xaVQ1cwGjmJkBpRCD_gOVF:18jh2a1qe"

}
web_data = requests.get(url,headers = headers)
Soup = BeautifulSoup(web_data.text,"lxml")
money = Soup.find_all()
for item in money:
    print(item)
