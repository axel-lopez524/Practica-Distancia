import math

class operasBas:   #todo lo que ponga aqui ya son propiedades
    n1=0
    n2=0
    res=0
    def sumar(self,a,b):  #le estamos pasando dos parametros
        self.res=self.n1+self.n2
        return self.res
    
    def pedirNumeros(self):
        self.n1=int(input("n1: "))
        self.n2=int(input("n2: "))
        print("La suma es: ",self.suma(self.n1,self.n2))
        
def main():
        
    obj= operasBas()

    obj.pedirNumeros()
    print("la suma es :",obj.sumar()) 
    
if__name__=="__main__":
    main()
    
          
