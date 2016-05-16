from bs4 import BeautifulSoup
import requests,re,urllib,os
urls = ["http://aiflb.com/shaonv/list_4_{}.html".format(str(i)) for i in range(1,100)]
next_url = []
count = 0
os.mkdir(r"C:/Users/子林/Pictures/福利")
def get_imgs(url):
    global next_url
    web_data = requests.get(urls[0])
    Soup = BeautifulSoup(web_data.text,"lxml")
    next_urls = Soup.select("div > div > div > div > h2 > a")
    for temp in next_urls:
        next_url.append("http://aiflb.com" + temp.get("href"))
def download_img(url):
    global count
    count = count + 1
    web_data = requests.get(url)
    Soup = BeautifulSoup(web_data.text, "lxml")
    download_imgs = Soup.select("div > div > center > div > img")[0].get("src")
    urllib.request.urlretrieve(download_imgs, "C:/Users/子林/Pictures/福利/" + str(count) + download_imgs[-4:])
    print(url)
def get_final_urls(url):
    web_data = requests.get(url)
    Soup = BeautifulSoup(web_data.text,"lxml")
    last_page = int(re.findall(r"\d+\.?\d*",Soup.select("div > div > div > a")[2].get_text())[0])
    for i in range(2,last_page + 1):
        temp = url[:-5]
        download_img(temp + "_" + str(i) + ".html")
for url1 in urls:
    get_imgs(url1)
    for url2 in next_url:
        get_final_urls(url2)




