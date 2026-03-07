import tkinter as Tk
from tkinter import messagebox

def calcular():
    try:
        num1 = float(entrada1.get())
        num2 = float(entrada2.get())
        operacion = opcion.get()
        
        if operacion == 1:
            resultado = num1 + num2
            
        elif operacion == 2:
            resultado = num1 - num2
            
        elif operacion == 3:
            resultado = num1 * num2
        
        elif operacion == 4:
            if num2 == 0:
                messagebox.showerror("Error, No se puede dividir entre 0")
                return
            resultado = num1 / num2
        else:
            messagebox.showwarning("Advertencia", "Seleccione una operacion")
            return
        etiqueta_resultado.config(text=f"Resultado: {resultado}")
        
    except ValueError:
        messagebox.showerror("Error", "Porfavor ingresa numeros validos")
        
#Ventana principal            
ventana = Tk.Tk()
ventana.title("Calculadora con Radiobotones")
ventana.geometry("350x300")

#Entradas
Tk.Label(ventana, text="Primer Numero:").pack(pady=5)
entrada1 = Tk.Entry(ventana)
entrada1.pack()

Tk.Label(ventana, text="Segundo Numero:").pack(pady=5)
entrada2 = Tk.Entry(ventana)
entrada2.pack()

#Variable para los radiobotones
opcion = Tk.IntVar()

Tk.Label(ventana, text="Selecciona la operacion:").pack(pady=10)

Tk.Radiobutton(ventana, text="Suma", variable=opcion, value=1).pack()
Tk.Radiobutton(ventana, text="Resta", variable=opcion, value=2).pack()
Tk.Radiobutton(ventana, text="Multiplicacion", variable=opcion, value=3).pack()
Tk.Radiobutton(ventana, text="Division", variable=opcion, value=4).pack()

#Boton para Calcular
Tk.Button(ventana, text="Calcular", command = calcular).pack(pady=10)

#Resultado
etiqueta_resultado = Tk.Label(ventana, text="Resultado")
etiqueta_resultado.pack()

ventana.mainloop()