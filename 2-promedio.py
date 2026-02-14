import math,os 

 
os.system("cls")

ico201 =[]

alumno1 = {
     "nombre": "",
    "edad": 0,
    "materia": "",
    "calificacion": ""
    
}

ico201 =[]

num=int(input("cuantos alumnos quiere ingresar?"))

for i in range(num):
    nombre = input("nombre de alumno: ")
    edad = int(input("edad del alumno: "))
    materia = input("nombre de la materia: ")
    calificacion = float(input("calificacion: "))
    
    alumno1["nombre"] = nombre
    alumno1["edad"] = edad
    alumno1["materia"] = materia
    alumno1["calificacion"] = calificacion
    ico201.append(alumno1.copy())
todas_las_calificaciones = 0   

 
todas_las_calificaciones = [alumno1["calificacion"] for alumno1 in ico201]   
print(todas_las_calificaciones)
print("promedio")

if len(todas_las_calificaciones) > 0:
    promedio = sum(todas_las_calificaciones) / num 
    
    print("El promedio general es: ",promedio)
    
else:
    print("no hay alumnos registrados")
    
print("lista de alumnos ingresados: ")