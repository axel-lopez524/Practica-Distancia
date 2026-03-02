import tkinter as tk

from tkinter import messagebox

def sumar():
    try:
        num1 = float(entrada1.get())
        num2 = float(entrada2.get())
        resultado = num1 + num2
        etiqueta_resultado.config(text=f"resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Error", "por favor ingresa un numero valido")    
#crear ventana principal
ventana= tk.Tk()
ventana.title("Calculadora de suma")
ventana.geometry("300x200")       

tk.Label(ventana, text="Primer numero:").pack(pady=5)

entrada1 = tk.Entry(ventana)
entrada1.pack()

tk.Label(ventana, text="Segundo numero numero:").pack(pady=5)
entrada2 = tk.Entry(ventana)
entrada2.pack()

tk.Button(ventana, text="suma", command= sumar).pack(pady=10)

etiqueta_resultado=tk.Label(ventana, text="Resultado: ")
etiqueta_resultado.pack()

ventana.mainloop()