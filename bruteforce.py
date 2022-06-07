from time import sleep
from selenium import webdriver
from sys import exit
import os

options = webdriver.ChromeOptions()
options.add_argument("--allow-file-access-from-files")
driver = webdriver.Chrome(chrome_options=options)
driver.get("") #local da pasta

wordlist = open("wordlist.txt", "r")
linhas = wordlist.read().split()

def enviarSenhas():
    requests = 0
    for x in range(len(linhas)):
        requests += 1
        os.system("cls")
        print("Testando a senha: " + str(linhas[x]))
        print("Total de requests: " + str(requests))
        try:
            driver.find_element_by_xpath('//*[@id="entrarSenha"]').send_keys(str(linhas[x]))
            driver.find_element_by_xpath('//*[@id="botao2"]').click()
            # alert = driver.switch_to.alert
            # alert.accept()
            driver.find_element_by_xpath('//*[@id="entrarSenha"]').clear()
        except:
            print("A senha é " + str(linhas[x]))
            exit()

input("Aperte enter para começar.")
while True:
    enviarSenhas()
    #sleep(1)