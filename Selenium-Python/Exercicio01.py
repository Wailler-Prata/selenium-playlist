from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from time import sleep

url = 'https://curso-python-selenium.netlify.app/exercicio_01.html'
navegador = Firefox()

def acessaNavegador(url):
navegador.get(url)
sleep(1)

def fecharNavegador():
navegador.quit()

def criaDicionario():

dic = {}
dic2 = {}
nH1 = navegador.find_elements_by_tag_name('H1')
paragrafos = navegador.find_elements_by_tag_name('p')

for n in range(3):
dic2.update({'Paragrafo' + str(n + 1): paragrafos[n].text})

dic.update({nH1[-1].text: dic2})
print(dic)


acessaNavegador(url = url)
criaDicionario()
fecharNavegador()