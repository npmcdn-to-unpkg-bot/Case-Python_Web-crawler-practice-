from bs4 import BeautifulSoup
import requests,urllib.request,time
urls = ["http://www.pptstore.net/pn{}/".format(str(i)) for i in range(100)]
all_webs = []
all_pics_webs = []
count = 0
def get_img(url):
    global count
    web_data = requests.get(url)
    Soup = BeautifulSoup(web_data.text,"lxml")
    single_web_data = Soup.select("#container > li > div > div.mod-bd > h3 > a")
    for item in single_web_data:
        all_webs.append(item.get("href"))
    for img_url in all_webs:
        web_data = requests.get(img_url)
        Soup = BeautifulSoup(web_data.text,"lxml")
        imgs = Soup.select("#gallery > div > div > ul > li")
        for it in imgs:
            img_str = str(it)
            count = count + 1
            urllib.request.urlretrieve(img_str[14:78].replace('_middle',""), "C:/Users/子林/Documents/Case-ppt/Creative_material/" + str(count) + img_str[74:78])
            print(img_str[14:78])
time_ = 0
for url in urls:
    if time_//2 == 0:
        time_ = time_ + 1
        time.sleep(1)
    get_img(url)

