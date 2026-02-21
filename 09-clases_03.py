import math , os

class areas:
    n1=0
    n2=0
    n3=0
    res=0
        
    def cuadrado(self):
        self.res=self.n1*self.n2
        c = self.res
        return self.res
    
    def rectangulo(self):
        self.res=self.n1*self.n2
        c=self.res
        return self.res
    
    def triangulo(self):
        self.res=(self.n1*self.n2)/2
        c =self.res
        return self.res
    
    def circulo(self):
        self.res=self.n1
        c= math.pi * (self.n1**2)
        return math.pi * (self.n1**2)
    
    def trapecio(self):
        self.res=(self.n1+self.n2) * (self.n3) / 2
        c=self.res
        return self.res
    
    def pedirNumeros(self, a):
        self.n1 = int(input("n1: "))
        self.n2 = int(input("n2: "))
        if a == 5:
            self.n3 = int(input("n3: "))

    def imprimir(self):
        print("El resultado es: ", self.res)
    
def main():
    
    obj= areas()
    
    op = 0
    while op != 6:
        os.system("cls")
        
        print("1.- cuadrado\n2.- rectangulo\n3.- triangulo\n4.- circulo\n5.- trapecio\n6.- salir")
        op = int(input("--opcion--: "))
        if op == 1:
            obj.pedirNumeros(0)
            obj.cuadrado()
            obj.imprimir()
            input()
        elif op == 2:
            obj.pedirNumeros(0)
            obj.rectangulo()
            obj.imprimir()
            input()
        elif op == 3:
            obj.pedirNumeros(0)
            obj.triangulo()
            obj.imprimir()
            input()
        elif op == 4:
            obj.pedirNumeros(0)
            obj.circulo()
            obj.imprimir()
            input()
        elif op == 5:
            obj.pedirNumeros(5)
            obj.trapecio()
            obj.imprimir()
            input()    
        elif op == 6:
            print("Obcion invalida: ")
        else:
            print("vuelve a intentarlo")

if __name__=="__main__":
    main()

