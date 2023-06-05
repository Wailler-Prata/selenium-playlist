from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.events import AbstractEventListener, EventFiringWebDriver
from time import sleep


class Escuta(AbstractEventListener):

    def before_click(self, element, webdriver):
        if label != '':
            print(webdriver.find_element(By.ID, 'l' + label).text)


    def after_click(self, element, webdriver):
        if label != '':
            print(webdriver.find_element(By.ID, 'l' + label).text)

    def after_navigate_to(self, url, webdriver):
        print('Indo para: ' + url)


def abreNavegador(browser, url):
    browser.get(url)

def fechaNavegador(browser):
    browser.quit()

def insereInformacoes(browser, dicionario):

    for info in dicionario.keys():

        # Global -> aqui defini a variavél "label" como global, dessa forma ela pode ser chamada em qualquer lugar
        global label
        label = info
        browser.find_element_by_css_selector('input[name="' + info + '"]').click()
        label = ''
        print(dicionario[info])
        browser.find_element_by_css_selector('input[name="' + info + '"]').send_keys(dicionario[info])

    browser.find_element(By.ID, 'btn').click()





url = 'https://selenium.dunossauro.live/exercicio_07.html'
firefox = firefoxSemEscuta = Firefox()

firefox = EventFiringWebDriver(firefox, Escuta())
dicionario = {'nome': 'Wailler', 'email': 'wailler@outlook.com', 'senha': '123456'}

abreNavegador(firefox, url)
sleep(2)
insereInformacoes(firefox, dicionario)
sleep(1)
fechaNavegador(firefox)