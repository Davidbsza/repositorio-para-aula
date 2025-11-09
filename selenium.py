from selenium import webdriver
import time

# abrir navegador
navegador = webdriver.Microsoft.Edge()

# Acessar um site
navegador.get("https://www.youtube.com")

#Colocar o navegador em tela cheia
navegador.maximize_window()

# Selecionar um elemento na tela
botao_login = navegador.find_element("/html/body/ytd-app/div[1]/div[2]/ytd-masthead/div[4]/div[3]/div[2]/ytd-button-renderer/yt-button-shape/a/yt-touch-feedback-shape/div[2]")
time.sleep(5)