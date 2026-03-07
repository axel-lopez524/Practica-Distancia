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
                messagebox.showerror("Error", "No se puede dividir entre 0")
                return
            resultado = num1 / num2
        else:
            messagebox.showwarning("Advertencia", "Seleccione una operación")
            return
            
        etiqueta_resultado.config(text=f"Resultado: {resultado}")
        
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa números válidos")

# Ventana principal
ventana = Tk.Tk()
ventana.title("Calculadora con Grid")
ventana.geometry("350x350")
ventana.config(padx=20, pady=20) # Margen interno para que no pegue al borde

# --- Entradas ---
Tk.Label(ventana, text="Primer Número:").grid(row=0, column=0, sticky="e", pady=5)
entrada1 = Tk.Entry(ventana)
entrada1.grid(row=0, column=1, pady=5)

Tk.Label(ventana, text="Segundo Número:").grid(row=1, column=0, sticky="e", pady=5)
entrada2 = Tk.Entry(ventana)
entrada2.grid(row=1, column=1, pady=5)

# --- Radiobotones ---
Tk.Label(ventana, text="Operación:").grid(row=2, column=0, pady=10, sticky="nw")

opcion = Tk.IntVar()

Tk.Radiobutton(ventana, text="Suma", variable=opcion, value=1).grid(row=3, column=0, padx=5, pady=5)
Tk.Radiobutton(ventana, text="Resta", variable=opcion, value=2).grid(row=4, column=0, padx=5, pady=5)
Tk.Radiobutton(ventana, text="Multiplicación", variable=opcion, value=3).grid(row=3, column=1, padx=5, pady=5)
Tk.Radiobutton(ventana, text="División", variable=opcion, value=4).grid(row=4, column=1, padx=5, pady=5)


Tk.Button(ventana, text="Calcular", command=calcular, width=15).grid(row=6, column=0, columnspan=2, pady=20)


etiqueta_resultado = Tk.Label(ventana, text="Resultado: ", font=("Arial", 10, "bold"))
etiqueta_resultado.grid(row=7, column=0, columnspan=2)

ventana.mainloop()