import requests
from bs4 import BeautifulSoup
from datetime import datetime

def coletar_cpi():
    url = "https://www.bls.gov/news.release/cpi.nr0.htm"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    tabela = soup.find("table")
    linhas = tabela.find_all("tr")[1:3]

    dados = []
    for linha in linhas:
        colunas = linha.find_all("td")
        if colunas:
            categoria = colunas[0].text.strip()
            valor = colunas[-1].text.strip()
            dados.append(f"{categoria}: {valor}")
    return "\n".join(dados)
