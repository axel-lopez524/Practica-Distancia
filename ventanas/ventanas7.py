import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

root = tk.Tk()
root.litle("Cerrar con confirmacion")
root.geometry("500x400")
def cerrar():
    respuesta = messagebox.askyesno("Salir", "¿Deseas cerrar la aplicacion?")
    if respuesta:
        root.destroy()
        
imagen = Image.open("UDL.png")
fondo = ImageTk.PhotoImage(imagen)

label_fondo= tk.Label(root, image=fondo)
label_fondo.place(x=0, y=0, relwidth=1, relheight=1 )

frame_acciones = tk.LabelFrame(root, text="Acciones", bg="#1E3A8A", fg="white", padx=10, pady=10)
frame_acciones.place(x=200, y=250, width=200, height=100)

tk.Button(frame_acciones, text="Salir", command=cerrar).pack(pady=20)

root.mainloop()