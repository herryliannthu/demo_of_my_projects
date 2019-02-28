import requests
import time
from bs4 import BeautifulSoup
import os
import re
import urllib.request
import json
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
def get_web_page(url,c):
    if c == 1 :
        time.sleep(6)
    else:
        time.sleep(3)
    resp = requests.get(url = url)
    if resp.status_code != 200:
        print ("Invalid url:" , resp.url,"status_code",resp.status_code)
        return None
    else:
        return resp.text
def href_pure(hr):
    if hr == None :
        return None
    else:
        hrs = str(hr)
        return "https://www.ted.com{}".format(hrs)
def get_view(urls,var):
    time.sleep(1)
    vr = get_web_page(urls,var)
    soup = BeautifulSoup(vr,"lxml")
    datad = soup.find(class_= " d:n f-w:700 f:.9 f:1@xxl c:white " )
    try:
        for d in datad.span:
            return (d.string.strip())
    except Exception as e :
        print ("get_view",e)
        return None
def get_articles (web):
    countd = 0
    articles = []
    count = 0
    soup = BeautifulSoup(get_web_page(web,0),"lxml")
    data = soup.find_all(class_ = "media__message")
    data_day = soup.find_all(class_ = "meta")
    for d in data:
        try :
            articles.append({"speaker":d.h4.string,"title":d.a.string.strip("\n"),"href":href_pure(d.a["href"])})
        except Exception as e:
            print ("get_article",e)
    for d_d in data_day:
        try :
            if (countd == 5):
                var = 1
                counted = 0
            else :
                var = 0
                countd += 1
            articles[count]["posted"] = d_d.find(class_="meta__val").string.strip("\n")
            articles[count]["Related tags"] = get_related_tags(articles[count]["href"])
            articles[count]["views"] = get_view(articles[count]["href"],var)
        except Exception as e:
            print ("get_article",e)
        count += 1
    return articles

def get_wed_dynamic(url):
    driver = webdriver.Chrome("D:\python\web_driver\chromedriver_win32\chromedriver.exe")
    driver.get(url)
    ButtonElement = driver.find_elements_by_xpath("//button")
    ActionChainsDriver = ActionChains(driver).click(ButtonElement[len(ButtonElement)-7])
    ActionChainsDriver.perform()
    time.sleep(3)
    html_text = driver.page_source
    driver.quit()
    return html_text
def get_related_tags(url):
    tags = []
    soup = BeautifulSoup(get_wed_dynamic(url),"lxml")
    for s in soup.find_all(class_="t-t:c"):
        tags.append(s.string)
    del tags[0:4]
    return tags

for n in range(6,79):
    url = "https://www.ted.com/talks?page={}".format(str(n))
    with open('progam{}.json'.format(str(n)), 'w', encoding='utf-8') as f:
        json.dump(get_articles(url), f, indent=2, sort_keys=True, ensure_ascii=False)





#%%
a = []
a.append({"e":1})
a.append({"d":2})
a[0]["f"] = 3
print (a[0])
