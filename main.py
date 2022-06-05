from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import requests
import os

# for crawlering apes on opensea
page_url = "https://opensea.io/assets/ethereum/0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d"

options = Options()
options.add_argument("--disable-notifications")

chrome = webdriver.Chrome('./chromedriver', options=options)

if not os.path.exists("apes"):
  os.mkdir("apes") 

for i in range(100):
  chrome.get(f"{page_url}/{i+1}")
  soup = BeautifulSoup(chrome.page_source, 'html.parser')
  img_url = soup.find("img", {"class": "Image--image"})["src"]
  img = requests.get(img_url)

  with open("./apes/" + str(i+1) + ".png", "wb") as file:  
      file.write(img.content)  


chrome.close()
