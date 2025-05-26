import tkinter as tk  
def calcular(operador):
    try:
        num1 = entrada1.get()  
        num2 = entrada2.get()  

        float(num1) 
        float(num2)  

        expresion = f"{num1} {operador} {num2}"  
        resultado = eval(expresion) 

        if float(resultado).is_integer():  
            resultado = int(resultado)
        resultado_var.set(f"Resultado: {resultado}")  
    except ZeroDivisionError:
        resultado_var.set("No se puede dividir por cero Maquina")  
    except:
        resultado_var.set("Ingresa solo numeros en los dos lugares viejo")  

def limpiar():
    entrada1.set("") 
    entrada2.set("")  
    resultado_var.set("")  

ventana = tk.Tk() 
ventana.title("Calculadora Piola")  
ventana.geometry("400x300")  

entrada1 = tk.StringVar()  
entrada2 = tk.StringVar()  
resultado_var = tk.StringVar()  

tk.Label(ventana, text="Ingresa el primer numero Loco:").pack(pady=5)
tk.Entry(ventana, textvariable=entrada1, font=("Arial", 14), justify="center").pack()

tk.Label(ventana, text="Ingresa el  segundo numero Loco:").pack(pady=5)
tk.Entry(ventana, textvariable=entrada2, font=("Arial", 14), justify="center").pack()

tk.Label(ventana, text="Elegi operacion Maquina:").pack(pady=10)

frame_botones = tk.Frame(ventana)
frame_botones.pack()

tk.Button(frame_botones, text="+", width=5, command=lambda: calcular("+")).grid(row=0, column=0, padx=5)
tk.Button(frame_botones, text="-", width=5, command=lambda: calcular("-")).grid(row=0, column=1, padx=5)
tk.Button(frame_botones, text="*", width=5, command=lambda: calcular("*")).grid(row=0, column=2, padx=5)
tk.Button(frame_botones, text="/", width=5, command=lambda: calcular("/")).grid(row=0, column=3, padx=5)

tk.Button(ventana, text="Limpiar", command=limpiar).pack(pady=10)

tk.Label(ventana, textvariable=resultado_var, font=("Arial", 14), fg="blue").pack(pady=10)

ventana.mainloop()
