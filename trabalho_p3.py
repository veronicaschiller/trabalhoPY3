from bs4 import BeautifulSoup;
import requests
header = {"User-Agent":
          "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}
# vanguarda
url_vanguard= "https://www.livrariavanguarda.com.br/vitrine/promocional?gclid=Cj0KCQjwwISlBhD6ARIsAESAmp6CuNHBPg1_P_-pn6AjM5zJ-WK-pyUavmLzIEkBXJhAVSQ3VZBZKiIaAnzUEALw_wcB"

vanguarda = requests.get(url_vanguard, headers=header)
vang_html = BeautifulSoup(vanguarda.content, "html.parser")
livros_vanguarda = vang_html.find_all("div", class_="product-item mb-0 mb-md-4")
# print(livros_vanguarda)
vanguarda_list=[]
for livros in livros_vanguarda:
    nome_livro = livros.find("p", class_="product-item__title mb-1").get_text()
    valor_promo = livros.find("ins", class_="product-price__current-price").get_text()
    vanguarda_list.append({"titulo":nome_livro, "preço": valor_promo})

    # print(vanguarda_list)
# dois Pontos

url_doisPontos = "https://www.doispontos.com.br/livros?O=OrderByBestDiscountDESC"
dois_pontos = requests.get(url_doisPontos, headers=header)
dp_html = BeautifulSoup(dois_pontos.content,"html.parser")
livro_dp = dp_html.find_all("div" ,class_="data")

DP_list =[]
for livros_dp in livro_dp: 
    nome_livro_dp = livros_dp.find("h3", class_="product-name").get_text()
    valor = livros_dp.find("div", class_="product-price")
    valor_promo_dp = valor.find("em", class_="product-price__best").get_text()
    DP_list.append({'titulo':nome_livro_dp ,'preço':valor_promo_dp})

lista_livros = []

for livro in DP_list:
    lista_livros.append({"titulo":livro['titulo'], "preço":livro["preço"]})

for livro in vanguarda_list:
    lista_livros.append({"titulo":livro['titulo'], "preço":livro["preço"]})

# print(lista_livros)

def titulo(msg, traco="*"):
    print(traco*40)
    print(msg)
    print(traco*40)

def lista_livros_oferta_vanguarda ():
    print("-"*40)
    titulo("lista de ofertas vanguarda")
    print("-"*40)
    print()
    print("Nome Livro*********************************************: Preço R$")
    for livros in vanguarda_list:
        print(f"{livros['titulo']:20} {livros['preço']}")

def lista_livros_ofertas_dp():
    print("-"*40)
    titulo("lista de ofertas vanguarda")
    print("-"*40)
    print()
    print("Nome Livro**********************************************: Preço R$")
         
    for livros in DP_list:
        print(f"{livros['titulo']:20} {livros['preço']}")

while True:
    print("-"*40)
    print("1 Loja vanguarda                                                   ")
    print("2 Loja Dois Pontos                           ")
    print("3 ranking de preços do box de brigertom                     ")
    print("4 estatistica de melhor preço de livro                      ")
    print("5 pesquisa                                                  ")
    print("6 Finalizar                                                 ")
    print("7 Finalizar                                                 ")
    print("-"*40)

    opcao = int(input('Opção: '))

    match opcao:
        case 1:
            lista_livros_oferta_vanguarda()
        case 2:
            lista_livros_ofertas_dp()
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