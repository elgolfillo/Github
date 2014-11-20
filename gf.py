# Autor: elgolfillo@gmail.com
# Proposito de extraer informacion de Google Finance
#
# PEDIR un valor
# Mostar la informacion de la cotizacion en el terminal
#
# realizar ahora la lectura desde la we con la funcion URL
#
# 



import webbrowser, urllib, re, os, time


class GFinance():

    gf = "https://www.google.com/finance?q="

    # Busca un valor y saca la informacion de la cotizacion: EJ: NYSE:TEF
    def openFinance(self):
        busquedaGoogle=raw_input("Escribe el valor a consultar: ")
        url_valor= self.gf + busquedaGoogle
        busqueda = urllib.urlopen(url_valor).read()
        
        datos = re.search('id="ref_(.*?)">(.*?)<',busqueda)
        t = time.localtime()
        
        if datos:
             tiempo =[t.tm_year,t.tm_mon,t.tm_mday,t.tm_hour, t.tm_min,t.tm_sec]
             print  tiempo
             print  busquedaGoogle +" --> "+ datos.group(2)
        else: 
             out = "No he podido encontrar nada con " + busquedaGoogle
             print out

        time.sleep(10)
#        os.system('cls')
#        while True:
#                valoracion(d1)
             
#        if __name__ == "__main__":
#         d1 = raw_input("Nombre de la Empresa: ")
#         os.system('cls')
#         valoracion(d1)
    
    def __init__(self):
        self.openFinance()

    
    
# Instanciar clase 
ibex = GFinance()