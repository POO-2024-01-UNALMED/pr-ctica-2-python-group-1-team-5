import tkinter as tk
from iuMain import ventanaPrincipal
from PIL import Image,ImageTk
import random
#Para cambiar entre ventanas



def irVentanaPrincipal():
    ventana.destroy()
    ventanaPrincipal.ventanaPrincipal()

def salir():
    ventana.quit()

def descripcion(frame):
    for widget in frame.winfo_children():
        widget.destroy()
        
    tk.Label(frame,text="Funeraria Rosario te brinda un servicio de calidad en tus ceremonias fúnebres").pack(pady=4)


def ventanaInicio():

    #Objeto tipo ventana
    global ventana , indiceValor, button100, imagenes, hojasVida, label00, label01, label10, label11, indiceImagenes, imagenesProyecto, indiceImagenP4, labelP4
    ventana = tk.Tk()
    ventana.geometry("600x400")


    #Generacion de los contenedores principales 
    #Frame principal izquierda (P1)
    frameIzquierda=tk.Frame(ventana, bg="#9fd5d1",bd=5,relief="ridge")
    frameIzquierda.pack(side="left",expand = True, fill ="both",padx=10,pady=10)
    #Frame principal izquierda (P2)
    frameDerecha=tk.Frame(ventana,bg="#9fd5d1",bd=5,relief="ridge")
    frameDerecha.pack(side="right",expand=True,fill="both",padx=5,pady=5)


    #Frame secundario arriba izquierda (P3)
    frameArribaIzquierda=tk.Frame(frameIzquierda,bg="white",bd=2, relief="groove")
    frameArribaIzquierda.place(relx=0.05,rely=0.05,relwidth=0.9,relheight=0.4) 

    # Lista de mensajes de bienvenida
    mensajes_bienvenida = [
        "¡Bienvenido a la aplicación!",
        "¡Hola! Esperamos que disfrutes de tu experiencia.",
        "¡Saludos! Prepárate para explorar nuestra app.",
        "¡Bienvenido de nuevo! Nos alegra verte.",
    ]
    
    # Selecciona un mensaje aleatorio
    mensaje_aleatorio = random.choice(mensajes_bienvenida)
    
    # Crear Label para mostrar el mensaje de bienvenida
    label_bienvenida = tk.Label(
        frameArribaIzquierda, 
        text=mensaje_aleatorio, 
        bg="#f0f0f0",  # Fondo claro para contraste
        fg="#333",     # Color de texto oscuro
        font=("Helvetica", 14, "bold"),  # Fuente más elegante
        wraplength=250,  # Limitar el largo del texto
        justify="center",
        padx=20,  # Padding interno para más espacio
        pady=20
    )

    label_bienvenida.pack(expand=True,fill = "both", padx=10, pady=10)

    #Objeto de menú
    menuPrincipal= tk.Menu(ventana)

    #Asocial el objeto
    ventana.config(menu = menuPrincipal)

    frmDescripcion =tk.Frame(frameArribaIzquierda)
    frmDescripcion.pack(pady=2)

    #Crear menu opciones
    opciones = tk.Menu(menuPrincipal, tearoff=0)
    menuPrincipal.add_cascade(label="Opciones",menu=opciones)
    opciones.add_command(label="Descripcion",command=lambda:descripcion(frmDescripcion)) #,command=mostrarDescripcion)
    opciones.add_separator()
    opciones.add_command(label="Salir",command=salir)
    

    #Frame secundario abajo izquierda (P4)
    imagenesProyecto = ["iuMain/imagenes/imagen1F.png","iuMain/imagenes/imagen2F.png","iuMain/imagenes/imagen3F.png","iuMain/imagenes/imagen4F.png","iuMain/imagenes/imagen5F.png"]
    indiceImagenP4 = 0
    imagen1 = Image.open(imagenesProyecto[0])
    imagen1 = ImageTk.PhotoImage(imagen1)
    frameAbajoIzquierda=tk.Frame(frameIzquierda,bg="white",bd=2, relief="groove")
    frameAbajoIzquierda.place(relx=0.05,rely=0.47,relwidth=0.9,relheight=0.5)
    frameArribaAbajoIzquierda=tk.Frame(frameAbajoIzquierda,bg="white")
    frameArribaAbajoIzquierda.place(relx=0.04,rely=0.04,relwidth=0.9,relheight=0.8)
    labelP4 = tk.Label(frameArribaAbajoIzquierda,image=imagen1, bg="white")
    labelP4.pack(expand=True,padx=5,pady=5,fill="both")
    labelP4.bind("<Leave>", cambiarImagenP4)
    btnPrincipal=tk.Button(frameAbajoIzquierda, text="Iniciar Aplicación", command=irVentanaPrincipal)
    btnPrincipal.pack(expand=True,anchor="s",padx=5,pady=5)

    #Frame secundario arriba derecha (P5)
    frameArribaDerecha=tk.Frame(frameDerecha,bg="white",bd=2, relief="groove")
    frameArribaDerecha.place(relx=0.05,rely=0.05,relwidth=0.9,relheight=0.4) 
    button100 = tk.Button(frameArribaDerecha, bg= "white", text="Hojas de vida de los desarrolladores", font=("Arial",8), wraplength=200,justify="center",anchor="center",command=cambiarHojaVidaeImagenes)
    button100.pack(expand= True, fill= "both", padx=5,pady=5)

    #Frame secundario abajo derecha (P6)
    frameAbajoDerecha=tk.Frame(frameDerecha,bg="white",bd=2, relief="groove")
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
    hojaVida2 = "Sebastian soy un estudiante de ingeniería de sistemas apasionado por la tecnología, los gatos, el jazz y las historias de fantasía.  Disfruta programar mientras escucha música y se sumerge en mundos imaginarios"
    hojaVida3 = "Soy Andrés Pérez, tengo 18 años y soy estudiante de Ingeniería de Sistemas en la Universidad Nacional de Colombia. Me gustan los videojuegos, los animales y mejorar mis habilidades en programación y tecnología"
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

def cambiarImagenP4(event):
    global indiceImagenP4, imagenesProyecto,labelP4
    ancho1 = labelP4.winfo_width()
    alto1 = labelP4.winfo_height()
    indiceImagenP4 = (indiceImagenP4+1) % len(imagenesProyecto)
    imagenP4 = Image.open(imagenesProyecto[indiceImagenP4]).resize((ancho1, alto1))
    imagenP4 = ImageTk.PhotoImage(imagenP4)
    labelP4.config(image=imagenP4)
    labelP4.image = imagenP4
