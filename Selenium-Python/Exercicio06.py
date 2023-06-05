from selenium.webdriver import Firefox
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep


def abreNavegador(browser, url):
    browser.get(url)

def fechaNavegador(browser):
    browser.quit()

def entraSaiCaixa(browser):
    ac = ActionChains(browser)
    caixa = browser.find_element(By.ID, 'caixa')
    titulo = browser.find_element(By.CLASS_NAME, 'centro > h1')

    ac.move_to_element(caixa)
    ac.click(caixa)
    ac.double_click(caixa)
    ac.context_click(caixa)
    ac.move_to_element(titulo)
    ac.perform()

def pega_acoes(browser):
    acoes = browser.find_element(By.CLASS_NAME, 'direita > textarea')
    print(acoes.text)






firefox = Firefox()
url = 'https://selenium.dunossauro.live/caixinha.html'
abreNavegador(firefox, url)
sleep(0.5)
entraSaiCaixa(firefox)
pega_acoes(firefox)