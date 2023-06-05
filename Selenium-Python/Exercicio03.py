from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from time import sleep
from urllib.parse import urlparse
from json import loads
from pprint import pprint


url = 'https://selenium.dunossauro.live/aula_05.html'
navegador = Firefox()

def abreNavegador(url):
    navegador.get(url)

def fechaNavegador():
    navegador.quit()

def preencheForm(dicionario):
    sleep(2)
    for chave in dicionario.keys():
        navegador.find_element(By.NAME, chave ).send_keys(dicionario[chave])

    navegador.find_element(By.NAME, 'btn').click()
    sleep(1)

def recuperaUrl(dicionario):
    url_parseada = urlparse(navegador.current_url)
    url = url_parseada.query.split('&')
    lista = []
    listaParametros = []

    for i in url:
        i = i.replace('%40', '@')
        if any(palavra in i for palavra in dicionario):
           lista.append(i)

    for j in dicionario.keys():
        listaParametros.append( j + '=' + dicionario[j])

    if listaParametros == lista:
        print('certo')
    else:
        print('errado')


dicionario = {'nome' : 'Wailler', 'email': 'wailler@hotmail.com', 'senha' : '12345', 'telefone' : '31996830919'}
abreNavegador(url)
preencheForm(dicionario)
recuperaUrl(dicionario)
fechaNavegador()