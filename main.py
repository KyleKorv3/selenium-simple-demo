from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import requests
import os

# for crawlering crypto logos for demo
page_url = "https://cryptologos.cc"
 
options = Options()
options.add_argument("--disable-notifications")

chrome = webdriver.Chrome('./chromedriver', options=options)
chrome.get(page_url)

soup = BeautifulSoup(chrome.page_source, 'html.parser')
cols = soup.find("div", {"class": "flex-grid"}).find_all("div", {"class": "col"})

if not os.path.exists("assets"):
  os.mkdir("assets") 

for col in cols:
  if (a_tag :=col.find("a")) != None:
    img_name = a_tag.find("div", {"class": "div-middle-text"}).text.split()[-2][1:-1]
    chrome.get(page_url + a_tag["href"])
    soup = BeautifulSoup(chrome.page_source, 'html.parser')
    img_url = soup.find("div", {"class": "crypto-logo-png-inner"}).find("img")["src"]

    img = requests.get(page_url + img_url)
    
    with open("./assets/" + img_name + ".png", "wb") as file:  
      file.write(img.content)  
