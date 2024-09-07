import tkinter as tk

#Objeto tipo ventana
ventana = tk.Tk()

#Objeto de menú
menuPrincipal= tk.Menu(ventana)

#Asocial el objeto
ventana.config(menu = menuPrincipal)

#Crear menu opciones
opciones = tk.Menu(menuPrincipal, tearoff=0)
menuPrincipal.add_cascade(label="Opciones",menu=opciones)
opciones.add_command(label="Descripcion") #,command=mostrarDescripcion)
opciones.add_separator()
opciones.add_command(label="Salir")

#Generacion de los contenedores principales 
#Frame principal izquierda (P1)
frameIzquierda=tk.Frame(ventana, bg="black",bd=2,relief="solid")
frameIzquierda.pack(side="left",expand = True, fill ="both",padx=5,pady=5)
#Frame principal izquierda (P2)
frameDerecha=tk.Frame(ventana,bg="black")
frameDerecha.pack(side="right",expand=True,fill="both",padx=5,pady=5)


#Frame secundario arriba izquierda (P3)
frameArribaIzquierda=tk.Frame(frameIzquierda,bg="white")
frameArribaIzquierda.place(relx=0.05,rely=0.05,relwidth=0.9,relheight=0.67) 

#Frame secundario abajo izquierda (P4)
frameAbajoIzquierda=tk.Frame(frameIzquierda,bg="white")
frameAbajoIzquierda.place(relx=0.05,rely=0.75,relwidth=0.9,relheight=0.2)


#Frame secundario arriba derecha (P5)
frameArribaDerecha=tk.Frame(frameDerecha,bg="white")
frameArribaDerecha.place(relx=0.05,rely=0.05,relwidth=0.9,relheight=0.4) 

#Frame secundario abajo derecha (P6)
frameAbajoDerecha=tk.Frame(frameDerecha,bg="white")
frameAbajoDerecha.place(relx=0.05,rely=0.47,relwidth=0.9,relheight=0.5) 

#Configuración del frame en cuadrícula 
# Configurar el frame inferior derecho para que tenga 2 filas y 2 columnas de igual tamaño
frameAbajoDerecha.grid_rowconfigure(0, weight=1)
frameAbajoDerecha.grid_rowconfigure(1, weight=1)
frameAbajoDerecha.grid_columnconfigure(0, weight=1)
frameAbajoDerecha.grid_columnconfigure(1, weight=1)

# Partir el frame en dos filas y dos columnas 
# Crear los sub-frames dentro del frame inferior derecho (cuadrícula 2x2)
frame00 = tk.Frame(frameAbajoDerecha, bg="purple", bd=2, relief="solid")
frame00.grid(row=0, column=0, padx=2, pady=2, sticky="nsew")

frame01 = tk.Frame(frameAbajoDerecha, bg="blue", bd=2, relief="solid")
frame01.grid(row=0, column=1, padx=2, pady=2, sticky="nsew")

frame10 = tk.Frame(frameAbajoDerecha, bg="blue", bd=2, relief="solid")
frame10.grid(row=1, column=0, padx=2, pady=2, sticky="nsew")

frame11 = tk.Frame(frameAbajoDerecha, bg="purple", bd=2, relief="solid")
frame11.grid(row=1, column=1, padx=2, pady=2, sticky="nsew")

ventana.mainloop()