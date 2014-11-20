


class Menu:
    enlaces=[]
    titulos=[]
    def cargaropcion(self,en,tit):
        self.enlaces.append(en)
        self.titulos.append(tit)

    def mostrar(self):   
        for indice in range(0,len(self.enlaces)):
            print '<a href="'+self.enlaces[indice]+'">'+self.titulos[indice]+'</a>'


menu1=Menu()
menu1.cargaropcion('http://www.google.com','Google')
menu1.cargaropcion('http://www.yahoo.com','Yahoo')
menu1.cargaropcion('http://www.live.com','Msn')
menu1.mostrar()