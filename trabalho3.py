from bs4 import BeautifulSoup
import requests
# urls
url_vanguarda = "https://www.livrariavanguarda.com.br/"
url_saraiva = "https://www.saraiva.com.br/"
# get das urls
vanguarda = requests.get(url_vanguarda)
saraiva = requests.get(url_saraiva)
# get do html
html_vanguarda = BeautifulSoup(vanguarda.content, "html.parser")
html_saraiva = BeautifulSoup(saraiva.content, "html.parser")
# formatação
tamplate_vanguarda = html_vanguarda.find("main", class_="main-content")
tamplate_saraiva = html_saraiva.find(
    "div", class_="flex flex-grow-1 w-100 flex-column")

card_livros_vanguarda = tamplate_vanguarda.find_all(
    "div", attrs={"slick-track"})

# funçoes
def titulo(txt):
    pass


def ofertas():
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
    print("ofertas                                                   ")
    print("ranking de preços do box de hp           ")
    print("ranking de preços do box de brigertom")
    print("estatistica de melhor preço de livro       ")
    print("pesquisa                                                 ")
    print("Finalizar                                                  ")
    print("-"*40)
    opcao = int(input("Opção: "))

    match opcao:
        case 1:
            pass
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
