# -*- coding: utf-8 -*- 
"""
from selenium import webdriver
import time
import urllib
import urllib2

import webbrowser

"""

class refresco(str):
    # Datos PAGINA 
    titulo = "AS"
    url = print str
    my_email = "Elgolfillo@gmail.com"
    #refreshrate = int(120)
     
    # Metodos
    
    # Abrir pagina con Chrome 
    def set_chrome(self): 
        self.pagina = "http://www.as.com/"
        self.hora = time.strftime("%H:%M:%S")
        
    # Método constructor 
    def __init__(self, str):
        print "TITULO DE LA PAGINA: " + self.titulo
        print "URL : " + str
        print "Autor : " + self.my_email
        
        #self.set_chrome()
        #self.open_chrome()
        
        print self.url

    
    
# Instanciar clase 
pagina_as = refresco("www.google.es")     