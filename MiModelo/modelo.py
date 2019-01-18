class Busqueda():

    def __init__(self, lis):
        self.lista = lis
        print(self.lista)

    #Adaptacion de busqueda binaria
    def busuedaB(self, elen):
        self.elemento= elen
        self.inf =0
        self.sup= len(self.lista)
        self.medio = int((self.inf+self.sup)/2)
        self.ubi = -1

        while (self.inf<= self.sup) and (self.ubi==-1):
            if self.elemento== self.lista[self.medio]:
                self.ubi=self.medio
            elif (self.elemento< self.lista[self.medio]):
                self.sup= self.medio-1
            else:
                self.inf= self.medio+1
            self.medio= int((self.inf+self.sup+1)/2)


        return self.ubi
















