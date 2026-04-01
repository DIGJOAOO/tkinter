import tkinter as tk
from tkinter import ttk, messagebox

def guardar():
    try:
        nombre_objeto = Nombre.get().strip()
        id_objeto = Id_objeto.get().strip()
        valor = precio.get().strip()
        stock_objeto = stock.get().strip()
        desc_objeto = desc.get().strip()

        if not nombre_objeto or not id_objeto or not valor or not stock_objeto or not desc_objeto:
            raise ValueError("No se permiten campos vacíos")

        valor = float(valor)
        stock_objeto = int(stock_objeto)

        arbol.insert("", "end", values=(nombre_objeto, id_objeto, desc_objeto, stock_objeto, valor))

        limpiar_campos()

    except ValueError as e:
        messagebox.showerror("Error", str(e))


def limpiar_campos():
    Nombre.delete(0, tk.END)
    Id_objeto.delete(0, tk.END)
    precio.delete(0, tk.END)
    stock.delete(0, tk.END)
    desc.delete(0, tk.END)


def borrar():
    selected = arbol.focus()
    if selected:
        arbol.delete(selected)
    limpiar_campos()


def seleccionar_item(event):
    selected = arbol.focus()
    if selected:
        valores = arbol.item(selected, "values")

        Nombre.delete(0, tk.END)
        Nombre.insert(0, valores[0])

        Id_objeto.delete(0, tk.END)
        Id_objeto.insert(0, valores[1])

        desc.delete(0, tk.END)
        desc.insert(0, valores[2])

        stock.delete(0, tk.END)
        stock.insert(0, valores[3])

        precio.delete(0, tk.END)
        precio.insert(0, valores[4])


def editar():
    try:
        selected = arbol.focus()
        if not selected:
            raise ValueError("Seleccioná un elemento para editar")

        nombre_objeto = Nombre.get().strip()
        id_objeto = Id_objeto.get().strip()
        valor = precio.get().strip()
        stock_objeto = stock.get().strip()
        desc_objeto = desc.get().strip()

        if not nombre_objeto or not id_objeto or not valor or not stock_objeto or not desc_objeto:
            raise ValueError("No se permiten campos vacíos")

        valor = float(valor)
        stock_objeto = int(stock_objeto)

        arbol.item(selected, values=(nombre_objeto, id_objeto, desc_objeto, stock_objeto, valor))

        limpiar_campos()

    except ValueError as e:
        messagebox.showerror("Error", str(e))


root = tk.Tk()
root.title("Inventario")
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
arbol.column("Descripción", anchor="center", width=150)
arbol.column("Stock", anchor="center", width=80)
arbol.column("Precio", anchor="center", width=80)

arbol.heading("Nombre", text="Nombre")
arbol.heading("ID", text="ID")
arbol.heading("Descripción", text="Descripción")
arbol.heading("Stock", text="Stock")
arbol.heading("Precio", text="Precio")

arbol.bind("<<TreeviewSelect>>", seleccionar_item)

Nombre_label.place(x=5, y=12)
Nombre.place(x=120, y=12)

Id_label.place(x=5, y=42)
Id_objeto.place(x=120, y=42)

precio_label.place(x=5, y=72)
precio.place(x=120, y=72)

stock_label.place(x=5, y=102)
stock.place(x=120, y=102)

desc_label.place(x=5, y=132)
desc.place(x=120, y=132)

guardar_boton.place(x=5, y=175)
editar_boton.place(x=90, y=175)
borrar_boton.place(x=175, y=175)

root.mainloop()