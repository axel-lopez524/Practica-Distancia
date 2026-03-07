import tkinter as tk

from tkinter import ttk

def mostrar_texto():
    texto= Entry.get()
    label_resultado.config(text=f"escribiste: {texto}")
    
    
ventana= tk.Tk()
ventana.litle("Ejemplo con Entry")
ventana.greometry("400x300")

entrada= tk.Entry(ventana, font=("Arial", 14))
entrada.pack(pady=20)

boton = ttk.Button(ventana, text="Enviar", command=mostrar_texto)
boton.pack()

label_resultado=ttk.Label(ventana, text="")
label_resultado.pack(pady=20)

ventana.mainloop()
