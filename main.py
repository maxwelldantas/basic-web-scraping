from urllib.request import urlopen
from bs4 import BeautifulSoup
from openpyxl import workbook

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    html = urlopen(
        "https://receita.economia.gov.br/acesso-rapido/agenda-tributaria/agenda-tributaria-2020/agenda-tributaria-janeiro-2020/dia-06-01-2020")
    bs = BeautifulSoup(html, 'html.parser')
    linhas = bs.find_all('tr', {'class': 'even'})
    #   print(linhas)

    # Imprime texto contido em cada linha ##
    for i in linhas:
        print(i.text)
    # Imprime o texto de cada uma das tags filhas ##
    for i in linhas:
        filhas = i.findChildren("td")
        print(filhas[0])
        print(filhas[1])
        print(filhas[2])

    codigo, descricao, periodo = [], [], []
    for i in linhas:
        children = i.findChildren("td")
        codigo.append(children[0].text)
        descricao.append(children[1].text)
        periodo.append(children[2].text)

    import pandas as pd

    df = pd.DataFrame({'Código': codigo, 'Descrição': descricao, 'Período': periodo})
    df.to_excel('/home/maxwelldantas/Documentos/teste.xlsx')
    print("Documento Excel gerado com sucesso")
