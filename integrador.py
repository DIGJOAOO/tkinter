import tkinter as tk
from tkinter import ttk

def guardar():
    global arbol
    nombre_objeto = Nombre.get()
    id_objeto = Id_objeto.get()
    valor = precio.get()
    stock_objeto = stock.get()
    desc_objeto = desc.get()
    diccionario_objetos = {"Nombre": nombre_objeto, "ID" : id_objeto, "Precio" : valor, "Stock" : stock_objeto, "Descripción" : desc_objeto}

    arbol.insert(
        "",                
        "end",             
        values=(
            diccionario_objetos["Nombre"],
            diccionario_objetos["ID"],
            diccionario_objetos["Descripción"],
            diccionario_objetos["Stock"],
            diccionario_objetos["Precio"]
        )
    )
def borrar():
    global nombre_objeto, id_objeto, valor, stock_objeto, desc_objeto, diccionario_objetos
    Nombre.delete(0, tk.END)
    Id_objeto.delete(0, tk.END)
    precio.delete(0, tk.END)
    stock.delete(0, tk.END)
    desc.delete(0, tk.END)

def editar():
    print("asd")

root = tk.Tk()
root.title("inventario")
root.geometry("1280x720")
root.resizable(False, False)


ingresar_objetos = tk.LabelFrame(root, text="Ingresar objetos")
ingresar_objetos.pack(side="left", expand=True, fill="both")

Nombre_label = tk.Label(ingresar_objetos, text="Nombre:")
Id_label = tk.Label(ingresar_objetos, text="ID del objeto:")
precio_label = tk.Label(ingresar_objetos, text="Precio:")
stock_label = tk.Label(ingresar_objetos, text="Stock:")
desc_label = tk.Label(ingresar_objetos, text="Descripción:")

Nombre = tk.Entry(ingresar_objetos)
Id_objeto = tk.Entry(ingresar_objetos)
precio = tk.Entry(ingresar_objetos)
stock = tk.Entry(ingresar_objetos)
desc = tk.Entry(ingresar_objetos)

guardar_boton = tk.Button(root, text="Guardar", command=guardar)
borrar_boton = tk.Button(root, text="Borrar", command=borrar)
editar_boton = tk.Button(root, text="Editar", command=editar)

mostrar_objetos = tk.LabelFrame(root, text="Mostrar objetos")
mostrar_objetos.pack(side="right", expand=True, fill="both")

arbol = ttk.Treeview(mostrar_objetos)
arbol.pack(side="left", expand=True, fill="both")
arbol["columns"] = ("Nombre", "ID", "Descripción", "Stock", "Precio")

arbol.column("#0", width=0, stretch=False)
arbol.column("Nombre", anchor="center", width=100)
arbol.column("ID", anchor="center", width=80)
arbol.column("Precio", anchor="center", width=80)
arbol.column("Stock", anchor="center", width=80)
arbol.column("Descripción", anchor="center", width=150)

arbol.heading("Nombre", text="Nombre")
arbol.heading("ID", text="ID")
arbol.heading("Precio", text="Precio")
arbol.heading("Stock", text="Stock")
arbol.heading("Descripción", text="Descripción")



Nombre_label.place(x=5, y=12)
Nombre.place(x=90, y=12)
Id_label.place(x=5, y=42)
Id_objeto.place(x=90, y=42)
precio_label.place(x=6, y=72)
precio.place(x=90, y=72)
stock_label.place(x=5, y= 102)
stock.place(x=90, y= 102)
desc_label.place(x=5, y=132)
desc.place(x=90, y=132)
guardar_boton.place(x=5, y=175)
editar_boton.place(x=90, y=175)
borrar_boton.place(x=175, y=175)


root.mainloop()