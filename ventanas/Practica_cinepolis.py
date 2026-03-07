import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def calcular_pago():
    try:
        nombre = entry_nombre.get()
        num_personas = int(entry_personas.get())
        num_boletos = int(entry_boletos.get())
        usa_tarjeta = tarjeta.get()
        
        if not nombre:
            messagebox.showwarning("Dato faltante", "Por favor, ingrese el nombre del comprador.")
            return
            
        limite_boletos = num_personas * 7
        if num_boletos > limite_boletos:
            messagebox.showerror("Límite excedido", f"No se pueden comprar más de {limite_boletos} boletos.")
            return

        precio_unidad = 12
        subtotal = num_boletos * precio_unidad
        descuento_cantidad = 0

        if num_boletos > 5:
            descuento_cantidad = subtotal * 0.15
        elif 3 <= num_boletos <= 5:
            descuento_cantidad = subtotal * 0.10
        
        monto_intermedio = subtotal - descuento_cantidad
        descuento_tarjeta = 0
        if usa_tarjeta == "Sí":
            descuento_tarjeta = monto_intermedio * 0.10
        
        total_final = monto_intermedio - descuento_tarjeta

        entry_salida_pago.config(state="normal")
        entry_salida_pago.delete(0, tk.END)
        entry_salida_pago.insert(0, f"${total_final:.2f}")
        entry_salida_pago.config(state="readonly")
                            
    except ValueError:
        messagebox.showerror("Error", "Ingrese valores numéricos válidos.")

def salir():
    root.destroy()

root = tk.Tk()
root.title("Practica Cinépolis")
root.geometry("700x450")

imagen = Image.open("imagen2.png")
imagen = imagen.resize((700, 450), Image.Resampling.LANCZOS)
fondo = ImageTk.PhotoImage(imagen)

label_fondo= tk.Label(root, image=fondo)
label_fondo.place(x=0, y=0, relwidth=1, relheight=1 )


 
color_azul = "#041422" 

ventana1 = tk.LabelFrame(root, text=" Entradas ", fg="white", bg=color_azul, font=("Arial", 12, "bold"))
ventana1.place(x=30, y=50, width=320, height=180)

tk.Label(ventana1, text="Nombre", bg=color_azul, fg="white").grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry_nombre = tk.Entry(ventana1)
entry_nombre.grid(row=0, column=1, padx=10, pady=5)

tk.Label(ventana1, text="Cantidad Compradores", bg=color_azul, fg="white").grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_personas = tk.Entry(ventana1, width=10)
entry_personas.insert(0, "1")
entry_personas.grid(row=1, column=1, padx=10, pady=5, sticky="w")

tk.Label(ventana1, text="Tarjeta Cineco", bg=color_azul, fg="white").grid(row=2, column=0, padx=10, pady=5, sticky="e")
tarjeta = tk.StringVar(value="No")
tk.Radiobutton(ventana1, text="Sí", variable=tarjeta, value="Sí", bg=color_azul, fg="white", selectcolor="black").place(x=150, y=70)
tk.Radiobutton(ventana1, text="No", variable=tarjeta, value="No", bg=color_azul, fg="white", selectcolor="black").place(x=210, y=70)

tk.Label(ventana1, text="Cantidad De Boletas", bg=color_azul, fg="white").grid(row=3, column=0, padx=10, pady=5, sticky="e")
entry_boletos = tk.Entry(ventana1, width=10)
entry_boletos.grid(row=3, column=1, padx=10, pady=5, sticky="w")


ventana2 = tk.LabelFrame(root, text=" Salidas ", fg="white", bg=color_azul, font=("Arial", 12, "bold"))
ventana2.place(x=420, y=80, width=250, height=100)

tk.Label(ventana2, text="Valor a Pagar", bg=color_azul, fg="white").pack(side="left", padx=10)
entry_salida_pago = tk.Entry(ventana2, state="readonly", width=15)
entry_salida_pago.pack(side="left", padx=10)

ventana3 = tk.LabelFrame(root, text=" Acciones ", fg="white", bg=color_azul, font=("Arial", 12, "bold"))
ventana3.place(x=400, y=280, width=220, height=80)

btn_procesar = tk.Button(ventana3, text="Procesar", command=calcular_pago)
btn_procesar.pack(side="left", padx=20, pady=10)

btn_salir = tk.Button(ventana3, text="Salir", command=salir)
btn_salir.pack(side="left", padx=20, pady=10)

root.mainloop()