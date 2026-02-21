

class persona:
    
    def inicializar(self,nom):
        self.nombre= nom
        
    def imprimir(self):
        print("nombre",self.nombre)
        
        
        
        
persona1=persona()  #crear un objeto
persona1.inicializar("pedro")
persona1.imprimir()

persona2=persona()  #crear otro objeto en la clase persona
persona2.inicializar("carla")
persona2.imprimir()

class operasBas:   #todo lo que ponga aqui ya son propiedades
    n1=0
    n2=0
    res=0
    def sumar(self,a,b):  #le estamos pasando dos parametros
        return a+b
    
    def pedirNumeros(self):
        self.n1=int(input("n1: "))
        self.n2=int(input("n2: "))
        print("La suma es: ",self.suma(self.n1,self.n2))
        
obj= operasBas()

obj.pedirNumeros()
        