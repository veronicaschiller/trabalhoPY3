from bs4 import BeautifulSoup
import requests
from time import sleep


from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# header = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36" }

produto = input("Qual produto deseja buscar? ")

navegador = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

url_renner = "https://www.lojasrenner.com.br/b?Ntt=" + produto

navegador.get(url_renner)
sleep(2)

html_renner = BeautifulSoup(navegador.page_source, "html.parser")


resultado_renner = html_renner.find_all("a", class_="ProductBox_productBox__juRuk")
resultado_renner2 = resultado_renner.find_all("div", class_="ProductBox_productInfo__EZDkP ")

for resulta in resultado_renner:
    if(resulta == True):
        print(resulta)
    else:
        break
sleep(2)
print(resultado_renner2)

