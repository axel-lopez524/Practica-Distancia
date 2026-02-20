import os

def suma():
    os.system("cls")
    a = int(input("Numero1: "))
    b = int(input("Numero2: "))
    res = a+b
    print("la suma es : ",res)
    input()
    
def resta():
    os.system("cls")
    a = int(input("Numero1: "))
    b = int(input("Numero2: "))
    res = a+b
    print("la suma es : ",res)
    input()
    
def menu():
    op=0
    while op !=5:
        os.system("cls")
        print("1.-+\n 2.- -\n 3.- *\n 4.- / \n 5 salir\n")
        op = int(input("opcion: "))
        if op==1:
            suma()
        if op ==2:
            resta()
            
if__name__("__main__"):
    menu()
        
            
            