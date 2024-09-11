import tkinter as tk
from iuMain import ventanaPrincipal
from PIL import Image,ImageTk
#Para cambiar entre ventanas



def irVentanaPrincipal():
    ventana.withdraw()
    ventanaPrincipal.ventanaPrincipal()

def ventanaInicio():

    #Objeto tipo ventana
    global ventana , indiceValor, button100, imagenes, hojasVida, label00, label01, label10, label11, indiceImagenes
    ventana = tk.Tk()
    ventana.geometry("600x400")
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
    btnPrincipal=tk.Button(frameAbajoIzquierda, text="Iniciar Aplicación", command=irVentanaPrincipal)
    btnPrincipal.pack(expand=True)

    #Frame secundario arriba derecha (P5)
    frameArribaDerecha=tk.Frame(frameDerecha,bg="white")
    frameArribaDerecha.place(relx=0.05,rely=0.05,relwidth=0.9,relheight=0.4) 
    button100 = tk.Button(frameArribaDerecha, bg= "white", text="Hojas de vida de los desarrolladores", font=("Arial",8), wraplength=200,justify="center",anchor="center",command=cambiarHojaVidaeImagenes)
    button100.pack(expand= True, fill= "both", padx=5,pady=5)

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
    label00 = tk.Label(frame00)
    label00.pack(fill="both", expand=True)


    frame01 = tk.Frame(frameAbajoDerecha, bg="blue", bd=2, relief="solid")
    frame01.grid(row=0, column=1, padx=2, pady=2, sticky="nsew")
    label01 = tk.Label(frame01)
    label01.pack(fill="both", expand=True)

    frame10 = tk.Frame(frameAbajoDerecha, bg="blue", bd=2, relief="solid")
    frame10.grid(row=1, column=0, padx=2, pady=2, sticky="nsew")
    label10 = tk.Label(frame10)
    label10.pack(fill="both", expand=True)

    frame11 = tk.Frame(frameAbajoDerecha, bg="purple", bd=2, relief="solid")
    frame11.grid(row=1, column=1, padx=2, pady=2, sticky="nsew")
    label11 = tk.Label(frame11)
    label11.pack(fill="both", expand=True)

    hojaVida1 = "Soy Violeta, una estudiante de Ingeniería de Sistemas de 19 años, apasionada por la tecnología y el desarrollo de software. Me interesa aprender y crecer en el campo de la informática. Disfruto de actividades que me permitan mejorar mis habilidades técnicas."
    hojaVida2 = "Sebastian"
    hojaVida3 = "Andrés"
    hojasVida = [hojaVida1, hojaVida2, hojaVida3]
    imagenes = ["iuMain/imagenes/imagen1.png","iuMain/imagenes/imagen2.png","iuMain/imagenes/imagen3.png","iuMain/imagenes/imagen4.png","iuMain/imagenes/imagen5.png","iuMain/imagenes/imagen6.png","iuMain/imagenes/imagen7.png","iuMain/imagenes/imagen8.png","iuMain/imagenes/imagen9.png","iuMain/imagenes/imagen10.png","iuMain/imagenes/imagen11.png","iuMain/imagenes/imagen12.png"]
    indiceValor = 0
    indiceImagenes = 0
    ventana.mainloop()

def cambiarHojaVidaeImagenes():
    global indiceValor, button100, imagenes, hojasVida, label00, label01, label10, label11,indiceImagenes
    button100.config(text=hojasVida[indiceValor])

    ancho = label00.winfo_width()
    alto = label00.winfo_height()

    # Redimensionar las imágenes según el tamaño de los labels
    imagen00 = Image.open(imagenes[indiceImagenes]).resize((ancho, alto))
    imagen00 = ImageTk.PhotoImage(imagen00)
    label00.config(image=imagen00)
    label00.image = imagen00

    imagen01 = Image.open(imagenes[(indiceImagenes+1) % len(imagenes)]).resize((ancho, alto))
    imagen01 = ImageTk.PhotoImage(imagen01)
    label01.config(image=imagen01)
    label01.image = imagen01

    imagen10 = Image.open(imagenes[(indiceImagenes+2) % len(imagenes)]).resize((ancho, alto))
    imagen10 = ImageTk.PhotoImage(imagen10)
    label10.config(image=imagen10)
    label10.image = imagen10

    imagen11 = Image.open(imagenes[(indiceImagenes+3) % len(imagenes)]).resize((ancho, alto))
    imagen11 = ImageTk.PhotoImage(imagen11)
    label11.config(image=imagen11)
    label11.image = imagen11

    # Actualizar los índices
    indiceValor = (indiceValor+1) % len(hojasVida)
    indiceImagenes = (indiceImagenes+4) % len(imagenes)
