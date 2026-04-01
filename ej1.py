import tkinter as tk
import math

def agregar_texto(valor):
    texto = entrada_var.get()
    if valor == 'C':
        entrada_var.set('')
        return
    if valor == '⌫':
        entrada_var.set(texto[:-1])
        return
    if valor == '√':
        calcular_raiz()
        return
    if valor == '×':
        valor = '*'
    if valor == '÷':
        valor = '/'
    if valor == '^':
        valor = '**'
    entrada_var.set(texto + valor)

def validar_expresion(expr):
    permitidos = set('0123456789+-*/(). ')
    for ch in expr:
        if ch not in permitidos:
            raise ValueError
    return True

def calcular():
    expr = entrada_var.get()
    try:
        if any(c.isalpha() for c in expr):
            raise ValueError
        validar_expresion(expr)
        resultado = eval(expr)
        entrada_var.set(str(resultado))
    except ZeroDivisionError:
        entrada_var.set('Error')
    except Exception:
        entrada_var.set('Error')

def calcular_raiz():
    expr = entrada_var.get()
    try:
        if any(c.isalpha() for c in expr):
            raise ValueError
        validar_expresion(expr)
        valor = float(eval(expr))
        if valor < 0:
            raise ValueError
        resultado = math.sqrt(valor)
        entrada_var.set(str(resultado))
    except ZeroDivisionError:
        entrada_var.set('Error')
    except Exception:
        entrada_var.set('Error')

ventana = tk.Tk()
ventana.title('Calculadora')
ventana.resizable(False, False)

entrada_var = tk.StringVar()

frame_superior = tk.Frame(ventana)
frame_superior.pack(fill='both', padx=8, pady=8)

entrada = tk.Entry(frame_superior, textvariable=entrada_var, font=('Arial', 24), bd=4, justify='right')
entrada.pack(fill='both', ipady=10)

frame_inferior = tk.Frame(ventana)
frame_inferior.pack(padx=8, pady=(0,8))

filas = [
    ['C', '⌫', '^', '√'],
    ['7', '8', '9', '÷'],
    ['4', '5', '6', '×'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+'],
]

for r, fila in enumerate(filas):
    for c, simbolo in enumerate(fila):
        if simbolo == '=':
            boton = tk.Button(frame_inferior, text=simbolo, width=6, height=2, font=('Arial', 18), command=calcular)
        else:
            boton = tk.Button(frame_inferior, text=simbolo, width=6, height=2, font=('Arial', 18), command=lambda v=simbolo: agregar_texto(v))
        boton.grid(row=r, column=c, padx=4, pady=4)

ventana.mainloop()
