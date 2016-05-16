from bs4 import BeautifulSoup
import requests,urllib.request,time
urls=["http://simpledesktops.com/browse/{}/".format(str(i)) for i in range(100)]
count = 0
def get_img_urls(url):
    web_data = requests.get(url)
    Soup = BeautifulSoup(web_data.text,"lxml")
    temps = []
    for data in Soup.find_all(href = True):
        if 'href="/browse/desktops/' in str(data):
            temps.append(str(data).split(">")[0])
    temps = list(set(temps))
    for temp in temps:
        temp = temp.split('"')
        img_url = "http://simpledesktops.com"+temp[1]
        web_data = requests.get(img_url)
        Soup = BeautifulSoup(web_data.text, "lxml")
        img_url = Soup.select("body > div.wrapper > div.container > div > div > div > div > a > img")[0].get("src")[:-17]
        global count
        count = count + 1
        urllib.request.urlretrieve(img_url,"C:/Users/子林/Documents/Case-ppt/Flat_Design/" + str(count) + img_url[-4:])
        print(img_url)
for url in urls:
    get_img_urls(url)
    time.sleep(1)