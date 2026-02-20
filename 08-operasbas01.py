import math, os

os.system("cls")

print("1-suma"
"/2-resta"
"/3-multiplicacion"
"/4-divicion/5-salir")
num = 0

while num !=5:
    num = int(input("que operacion deseas realizar: "))
    a = int(input("coloca el primer numero: "))
    b = int(input("coloca el segundo numero: "))
    if num == 1:
        def suma():
            
            c = a+b
            return c
        print( suma())
    
    elif num == 2:
        def resta():
            c = a-b
            return c
        print(resta())
    
    elif num == 3:
        def mult():
            c = a*b
            return c
        print(mult())
    
    elif num == 4:
        def div():
            c = a / b
            return c
        print(div())
        
    else:
        print("salir")
   
