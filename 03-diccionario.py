alumno = {
    "nombre": "ana",
    "edad": 21,
    "carrera": "ingenieria"
    
}
print(type(alumno))
print(alumno)

print("print(alumno['nombre']) = ",alumno["nombre"])
print("print(alumno.get('edad')) = ",alumno.get("edad"))

'''Agregar o modificar valores'''
alumno["promedio"] = 9.2
print(alumno)
alumno["edad"] = 22

del alumno["carrera"]
print(alumno)


for clave in alumno:
    print(clave,":", alumno[clave])
    
print("Cantidadde pares claves-valor: ",len(alumno))
print("Claves de diccionarion: ",alumno.keys())
print("Valores del diccionario: ",alumno.values())
print("Pares claves-valor: ",alumno.items())

alumno1 = {
     "nombre": "",
    "edad": 0,
    "carrera": ""
    
}

ico201 = [alumno1,alumno1,alumno1]


