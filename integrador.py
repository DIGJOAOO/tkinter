import tkinter as tk


root =tk.Tk()
root.title("inventario")
root.geometry("1280x720")
root.resizable(False, False)


ingresar_objetos = tk.LabelFrame(root, text="Ingresar objetos")
ingresar_objetos.pack(side="left", expand=True, fill="both")

Nombre_label = tk.Label(ingresar_objetos, text="Nombre:")
ID_label = tk.Label(ingresar_objetos, text="ID del objeto:")
precio_label = tk.Label(ingresar_objetos, text="Precio:")
stock_label = tk.Label(ingresar_objetos, text="Stock:")

Nombre = tk.Entry()
ID_objeto = tk.Entry()
precio = tk.Entry()
stock = tk.Entry()

mostrar_objetos = tk.LabelFrame(root, text="Mostrar objetos")
mostrar_objetos.pack(side="right", expand=True, fill="both")

Nombre.place(x=5, y=30)
ID_objeto.place(x=5, y=60)
precio.place(x=5, y=90)
stock.place(x=5, y=120)

root.mainloop()