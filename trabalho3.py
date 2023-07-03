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
def titulo(txt , traco="-"):
    print()
    print(txt)
    print(traco * len(txt))
    pass


def ofertas():
    titulo("busca ofertas - melhor valor ")
    # pesq  valor 
    nome_livro = input("Qual livro deseja ver o melhor preço? ");
# loop
    for livro in nome_livro:
        livro = livro.strip()
        url_vanguarda = f"https://www.livrariavanguarda.com.br/busca/" + nome_livro
        url_submarino = f"https://www.submarino.com.br/busca/" + nome_livro
        # vanguarda resposta
        loja_vanguarda= requests.get(url_vanguarda)
        busca_vanguarda = loja_vanguarda.content
        soup_vanguarda = BeautifulSoup(busca_vanguarda,"html.parser")
        reusltado_vanguarda = soup_vanguarda.find("div", class_="product-item")
        # submarino resposta
        loja_submarino= requests.get(url_submarino)
        busca_submarino = loja_submarino.content
        soup_submarino = BeautifulSoup(busca_submarino,"html.parser")
        reusltado_submarino = soup_submarino.find("div", class_="vtex-slider-layout")

        print(reusltado_submarino)

    armazena_valore =[]

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
