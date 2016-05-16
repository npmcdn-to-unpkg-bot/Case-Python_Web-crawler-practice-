import requests
from bs4 import BeautifulSoup
import http.cookies
url = "http://210.29.96.239"
headers = {
    "Cookie":"JSESSIONID=cdagxFQ-9qLh-64UOIfqv",
    "Referer":"http://210.29.96.239/loginAction.do",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36"

}
web_data = requests.post(url,headers = headers)
Soup = BeautifulSoup(web_data.text,"lxml")
print(Soup)
