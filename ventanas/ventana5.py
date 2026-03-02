import tkinter as tk
from tkinter import messagebox

# Función para sumar
def sumar():
    try:
        num1 = float(entrada1.get())
        num2 = float(entrada2.get())
        resultado = num1 + num2
        etiqueta_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese números válidos")

# Crear ventana
ventana = tk.Tk()
ventana.title("Calculadora de Suma")
ventana.geometry("300x200")

# Etiquetas
tk.Label(ventana, text="Primer número:").grid(row=0, column=0, padx=5, pady=5)
tk.Label(ventana, text="Segundo número:").grid(row=1, column=0, padx=5, pady=5)

# Entradas (separar creación y grid)
entrada1 = tk.Entry(ventana)
entrada1.grid(row=0, column=1, padx=5, pady=5)

entrada2 = tk.Entry(ventana)
entrada2.grid(row=1, column=1, padx=5, pady=5)

# Botón
tk.Button(ventana, text="Sumar", command=sumar).grid(row=2, column=0, columnspan=2, pady=10)

# Resultado
etiqueta_resultado = tk.Label(ventana, text="Calcular :")
etiqueta_resultado.grid(row=3, column=0, columnspan=2, pady=10)

# Ejecutar aplicación
ventana.mainloop()