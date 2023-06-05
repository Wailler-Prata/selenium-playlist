from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from pprint import pprint
from time import sleep

url = 'https://selenium.dunossauro.live/exercicio_05.html'
firefox = Firefox()

def abreBrowser(browser, url):
    browser.get(url)

def fechaBrowser(browser):
    browser.quit()

def escopoExercicio(browser):
    exercicio = browser.find_element(By.TAG_NAME, 'span')
    return exercicio.text

def preencheForm(browser, form, dicionario):
    nome = browser.find_element_by_css_selector('.form-' + form + ' input[name="nome"]').send_keys(dicionario['name'])
    senha = browser.find_element_by_css_selector('.form-' + form + ' input[name="senha"]').send_keys(dicionario['password'])
    form = browser.find_element_by_css_selector('.form-' + form + ' input[name="' + form + '"]').click()




dicionario = {'name' : 'Wailler', 'password': '123456'}
abreBrowser(firefox, url)
sleep(1)
preencheForm(firefox, escopoExercicio(firefox), dicionario)
fechaBrowser(firefox)