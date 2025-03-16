# Tarea: Creación de una Aplicación GUI Básica
# Objetivo: Desarrollar una aplicación de interfaz gráfica de usuario (GUI) que permita a los usuarios interactuar con datos de manera visual.

import tkinter as tk
from tkinter import messagebox

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Aplicación de Gestión de Información")

# Crear una lista para almacenar la información ingresada
datos = []

# Función para agregar información
def agregar_dato():
    dato = campo_texto.get()
    if dato != "":
        datos.append(dato)
        actualizar_lista()
        campo_texto.delete(0, tk.END)  # Limpiar campo de texto después de agregar
    else:
        messagebox.showwarning("Entrada vacía", "Por favor, ingrese algún dato.")

# Función para limpiar la entrada de texto y la lista
def limpiar():
    campo_texto.delete(0, tk.END)
    lista_datos.delete(0, tk.END)

# Función para actualizar la lista mostrada
def actualizar_lista():
    lista_datos.delete(0, tk.END)
    for dato in datos:
        lista_datos.insert(tk.END, dato)

# Crear componentes GUI
etiqueta = tk.Label(ventana, text="Ingrese un dato:")
etiqueta.grid(row=0, column=0, padx=10, pady=10)

campo_texto = tk.Entry(ventana)
campo_texto.grid(row=0, column=1, padx=10, pady=10)

boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_dato)
boton_agregar.grid(row=1, column=0, padx=10, pady=10)

boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar)
boton_limpiar.grid(row=1, column=1, padx=10, pady=10)

# Crear lista para mostrar los datos agregados
lista_datos = tk.Listbox(ventana, width=30, height=10)
lista_datos.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Ejecutar la aplicación
ventana.mainloop()
