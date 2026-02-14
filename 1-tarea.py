import math,os 

 
os.system("cls")


alumno1 = {
     "nombre": "",
    "edad": 0,
    "carrera": ""
    
}

ico201 =[]

num=int(input("cuantos alumnos quiere ingresar?"))

for i in range(0,num):
    nombre= input("nombre de alumno: ")
    edad = int(input("edad del alumno: "))
    carrera= input("carrera del alumno: ")
    
    alumno1["nombre"] = nombre
    alumno1["edad"] = edad
    alumno1["carrera"] = carrera
    
    ico201.append(alumno1.copy())
    
print("lista de alumnos ingresados: ")

