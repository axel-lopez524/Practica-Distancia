import tkinter as tk

#creamos la ventana principal
def saludo():
    label_resultado.config(text="Hola alumnos de python")
    
ventana= tk.Tk()
ventana.title("Ejemplo con votones")
ventana.geometry("400x300")
    
    
boton=tk.botton(ventana, text="saludar", command= saludo)
boton.pack(pady=20)
    
    


#creamos una etiqueta 
label_resultado = tk.Label(ventana, text="", font=("Arial",16,"bold"))
label_resultado.pack(pady=20)
#mostramos la etiqueta en la ventana
ventana.mainloop()
