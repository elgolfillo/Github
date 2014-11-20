# -*- coding: utf-8 -*- 

from selenium import webdriver
import time
import urllib
import urllib2

import webbrowser


class Refresh():
    # Datos PAGINA 
    titulo = "AS"
    url = "http://www.as.com/"
    my_email = "Elgolfillo@gmail.com"
    #refreshrate = int(120)
     
    # Metodos
    
    # Abrir pagina con Chrome 
    def set_chrome(self): 
        self.pagina = "http://www.as.com/"
        self.hora = time.strftime("%H:%M:%S")

    # Calcula el monto total del presupuesto 
    def open_chrome(self): 
        webbrowser.open(self.pagina)
   
   # realiza el refresco de la pagina y abierta
    def refresco(self,pag):
        x=pag
        #x=raw_input("Enter the URL")
        refreshrate=raw_input("Enter the number of seconds")
        refreshrate=int(refreshrate)
        driver = webdriver.firefox()
        driver.get("http://"+x)
        while True:
            time.sleep(refreshrate)
            driver.refresh()
       
    # Método constructor 
    def __init__(self):
        print "TITULO DE LA PAGINA: " + self.titulo
        
        print "URL : " + self.url

        print "Autor : " + self.my_email
        
       # self.set_chrome()
        #self.open_chrome()
        
        pagina="www.google.es"
        self.refresco(pagina)

    
    
# Instanciar clase 
pagina_as = Refresh()
     