#autor: elgolfillo@gmail.com
# Proposito de conectar con Google Finance
#http://infostatex.blogspot.com.es/2014/07/python-y-google-finance-obteniendo.html
#
# PEDIR un valor
# Mostar la informacion Via WEB
#
#
#
#



import webbrowser

class GFinance():

    gf = "https://www.google.com/finance?q="

    
    def openFinance(self):
        valor=raw_input("Escribe el valor a consultar: ")
        valor= self.gf + valor
        webbrowser.open(valor)
        
    
    def __init__(self):
        self.openFinance()

    
    
# Instanciar clase 
ibex = GFinance()