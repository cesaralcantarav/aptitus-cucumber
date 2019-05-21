from selenium import webdriver
from  web.web import Web
import os

def get_web(browser):
    ruta = os.getcwd()
    if browser =="chrome":
        return Web(webdriver.Chrome(ruta + "/drivers/chromedriver"))