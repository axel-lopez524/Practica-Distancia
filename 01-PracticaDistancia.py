import math,os 

 
os.system("cls")

x1 = int(input("Ingrese x1: ")) 

y1 = int(input("Ingrese y1: ")) 

x2 = int(input("Ingrese x2: ")) 
y2 = int(input("Ingrese y2: ")) 

distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print("La Distacia Es: ",distancia)