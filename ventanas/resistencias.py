import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk

bandas = {
    "Negro": 0,
    "Cafe": 1,
    "Rojo": 2,
    "Naranja": 3,
    "Amarillo": 4,
    "Verde": 5,
    "Azul": 6,
    "Violeta": 7,
    "Gris": 8,
    "Blanco": 9
}

multiplicador = {
    "Negro": 1,
    "Cafe": 10,
    "Rojo": 100,
    "Naranja": 1000,
    "Amarillo": 10000,
    "Verde": 100000,
    "Azul": 1000000,
    "Violeta": 10000000,
    "Gris": 100000000,
    "Blanco": 1000000000
}

tolerancia = {
    "Oro": 0.05,
    "Plata": 0.10
}

def calculo():
   
    b1 = combo1.get()
    b2 = combo2.get()
    b3 = combo3.get()
    
    if opcion.get() == 1:
        tol = "Plata"
    elif opcion.get() == 2:
        tol = "Oro"
    else:
        messagebox.showerror("Error", "Selecciona una tolerancia")
        return
    
    # Calcular resistencia nominal
    valor = (bandas[b1] * 10 + bandas[b2]) * multiplicador[b3]
    
    # Calcular rango con tolerancia
    minimo = valor * (1 - tolerancia[tol])
    maximo = valor * (1 + tolerancia[tol])
    
    # Mostrar resultado
    messagebox.showinfo(
        "Resultado",
        f"Valor nominal: {valor} Ω\n"
        f"Valor mínimo: {minimo:.0f} Ω\n"
        f"Valor máximo: {maximo:.0f} Ω"
    )

# ---------------- INTERFAZ ----------------
ventana = tk.Tk()
ventana.title("Calculadora de Resistencias")
ventana.geometry("1000x350")


# Banda 1
tk.Label(ventana, text="Selecciona Color 1").grid(row=0, column=0, padx=10, pady=5)
combo1 = ttk.Combobox(ventana, values=list(bandas.keys()))
combo1.grid(row=0, column=1, padx=10, pady=5)

# Banda 2
tk.Label(ventana, text="Selecciona Color 2").grid(row=1, column=0, padx=10, pady=5)
combo2 = ttk.Combobox(ventana, values=list(bandas.keys()))
combo2.grid(row=1, column=1, padx=10, pady=5)

# Banda 3 (multiplicador)
tk.Label(ventana, text="Selecciona Color 3").grid(row=2, column=0, padx=10, pady=5)
combo3 = ttk.Combobox(ventana, values=list(multiplicador.keys()))
combo3.grid(row=2, column=1, padx=10, pady=5)

# Tolerancia
opcion = tk.IntVar()
tk.Label(ventana, text="Tolerancia").grid(row=3, column=0, padx=10, pady=5)
ttk.Radiobutton(ventana, text="Plata", variable=opcion, value=1).grid(row=3, column=1)
ttk.Radiobutton(ventana, text="Oro", variable=opcion, value=2).grid(row=3, column=2)

# Botón calcular
btn_calcular = tk.Button(ventana, text="Calcular", command=calculo)
btn_calcular.grid(row=4, column=1, pady=20)

ventana.mainloop()

