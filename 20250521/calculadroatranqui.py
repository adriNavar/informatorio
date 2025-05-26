import tkinter as tk

def calcular():
    expresion = entrada.get()
    caracteres_permitidos = "0123456789+-*/. "
    
    try:
        if all(char in caracteres_permitidos for char in expresion):
            resultado = eval(expresion)
            resultado_var.set(f"Resultado: {resultado}")
        else:
            resultado_var.set("Solo se permiten números y (+ - * /)")
    except:
        resultado_var.set("Error en la expresión")

def limpiar():
    entrada.set("")
    resultado_var.set("")

ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("350x250")

entrada = tk.StringVar()
resultado_var = tk.StringVar()

tk.Label(ventana, text="Ingrese una expresión matemática:").pack(pady=10)
tk.Entry(ventana, textvariable=entrada, font=("Arial", 14), justify="center", width=25).pack(pady=5)

tk.Button(ventana, text="Calcular", command=calcular).pack(pady=5)
tk.Button(ventana, text="Limpiar", command=limpiar).pack(pady=5)

tk.Label(ventana, textvariable=resultado_var, font=("Arial", 14), fg="blue").pack(pady=10)

ventana.mainloop()