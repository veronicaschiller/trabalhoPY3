from bs4 import BeautifulSoup
import requests

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}
# urls
url_vanguarda = "https://www.livrariavanguarda.com.br/"
url_saraiva = "https://www.saraiva.com.br"
# get das urls
vanguarda = requests.get(url_vanguarda, headers=header)
saraiva = requests.get(url_saraiva, headers=header)
# get do html
html_vanguarda = BeautifulSoup(vanguarda.content, "html.parser")
html_saraiva = BeautifulSoup(saraiva.content, "html.parser")

url_vanguarda = "https://www.livrariavanguarda.com.br/vitrine/promocional"
url_saraiva = "https://www.saraiva.com.br/livros/gastronomia?order=OrderByBestDiscountDESC"
# vanguarda resposta
loja_vanguarda = requests.get(url_vanguarda, headers=header)
soup_vanguarda = BeautifulSoup(loja_vanguarda.content, "html.parser")
reusltado_vanguarda = soup_vanguarda.find_all("div", class_="product-item mb-0 mb-md-4")
# saraiva resposta
loja_saraiva = requests.get(url_saraiva, headers=header)
soup_saraiva = BeautifulSoup(loja_saraiva.content, "html.parser")
reusltado_saraiva = soup_saraiva.find_all(
    "a", attrs={"aria-current":"page"}
)

armazena_valore = []

for lista in reusltado_vanguarda:
    titulo = lista.find("p" , class_="product-item__title mb-1").a.get_text()
    preco = lista.find("ins", class_="product-price__current-price").i.get_text()
    armazena_valore.append({"titulo":titulo , "preço" : preco})

for lista in reusltado_saraiva:
    preco2 = lista.find("div", class_="price-info__Wrapper-sc").span.get_text()
    print(preco2)

# funçoes
def titulo(txt, traco="-"):
    print()
    print(txt)
    print(traco * len(txt))
    pass


def ofertas():
    titulo("busca ofertas - melhor valor ")
    

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
    print("-" * 40)
    print("1 ofertas                                                   ")
    print("2 ranking de preços do box de hp                            ")
    print("3 ranking de preços do box de brigertom                     ")
    print("4 estatistica de melhor preço de livro                      ")
    print("5 pesquisa                                                  ")
    print("6 Finalizar                                                 ")
    print("-" * 40)

    opcao = int(input("Opção: "))

    if opcao == 1:
        ofertas()
    elif opcao == 2:
        pass
    elif opcao == 3:
        pass
    elif opcao == 4:
        pass
    elif opcao == 5:
        pass
    elif opcao == 6:
        pass
    else:
        print()
        print("obgda por pesquisar!")
        print()
        break
