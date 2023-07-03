from bs4 import BeautifulSoup
import requests

from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

navegador = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# headers
header = {"User-Agent":
          "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}


def titulo(txt, traco="-"):
    print()
    print(txt)
    print(traco*len(txt))
    pass


def ofertas():
    titulo("busca ofertas - melhor valor ")
    # pesq  valor
    nome_livro = input("Qual livro deseja ver o melhor preço? ")
# loop

    url_vanguarda = f"https://www.livrariavanguarda.com.br/busca/" + nome_livro
    url_submarino = f"https://www.submarino.com.br/busca/" + nome_livro

    # vanguarda resposta
    navegador.get(url_vanguarda)
    soup_vanguarda = BeautifulSoup(navegador.page_source, "html.parser")
    reusltado_vanguarda = soup_vanguarda.find_all(
        "div", class_="product-item mb-0 mb-md-4")

    # submarino resposta
    navegador.get(url_submarino)
    soup_submarino = BeautifulSoup(navegador.page_source, "html.parser")
    print(soup_submarino)
    titulo_livro = soup_submarino.find_all()
    # reusltado_submarino = soup_submarino.fin("div", class_="vtex-slider-layout")
    print(titulo_livro)

    armazena_valore = []

    pass


def rankin_box_hp():
    pass


def ranking_box_brigerton():
    pass


def estatistica():
    pass


def pesq():
    pass


while True:
    print("-"*40)
    print("1 ofertas                                                   ")
    print("2 ranking de preços do box de hp                            ")
    print("3 ranking de preços do box de brigertom                     ")
    print("4 estatistica de melhor preço de livro                      ")
    print("5 pesquisa                                                  ")
    print("6 Finalizar                                                 ")
    print("-"*40)

    opcao = int(input('Opção: '))

    match opcao:
        case 1:
            ofertas()
        case 2:
            pass
        case 3:
            pass
        case 4:
            pass
        case 5:
            pass
        case 7:
            print("Obrigado por busacar com a gente!")
            print()
            break