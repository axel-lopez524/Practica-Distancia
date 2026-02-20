import math, os

def cuadrado():
    os.system("cls")
    a = int(input("Ingrese el primer lado: "))
    b = int(input("Ingrese el segundo lado: "))
    return a*b


def rectangulo():  
    os.system("cls")
    a = int(input("Ingrese la base: "))
    b = int(input("Ingrese la altura: "))
    c = a * b
    return a*b
    
    
def triangulo():
    os.system("cls")
    a = int(input("Ingrese la base: "))
    b = int(input("Ingrese la altura: "))
    c = (a*b)/2
    return (a*b)/2
def circulo():
    os.system("cls")
    a = float(input("Ingrese el radio: "))
    c = math.pi * (a**2)
    return math.pi * (a**2)

def trapecio():
    os.system("cls")
    a = int(input("Ingrese la base mayor: "))
    b = int(input("Ingrese la base menor: "))
    c = int(input("Ingrese la altura: "))
    c = ((a+b) * (c)) /2
    return (a+b) * (c) /2
def menu():
    opcion = 0
    while opcion != 6:
        print("\n-menu-")
        
        print("1.- cuadrado\n2.- rectangulo\n3.- triangulo\n4.- circulo\n5.-trapecio\n6.- salir")
        
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            print("El area es:", cuadrado())
        
        elif opcion == 2:
            print("El area es:", rectangulo())
        
        elif opcion == 3:
            print("El area es:", triangulo())
        
        elif opcion == 4:
            print("El area es:", circulo())
        
        elif opcion == 5:
            print("El area es:", trapecio())
        
        elif opcion == 6:
            print("Saliendo del programa...")
        else:
            print("Opción inválida, intente de nuevo.")
        
        
if __name__("__Main__"):
    menu()

menu()


        
        
        
        
        
    