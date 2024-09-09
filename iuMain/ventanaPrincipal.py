import tkinter as tk
from iuMain import ventanaInicio
from iuMain.funcionalidades import cremacion

#Regresar a la ventana de inicio
def irVentanaInicio():
    ventana.withdraw()
    ventanaInicio.ventanaInicio()

#Aplicacion
def aplicacion():
    ventanaDescripcion = tk.Toplevel()
    ventanaDescripcion.title("Funeraria Rosario")
    ventanaDescripcion.geometry("500x500")

    texto= """
        Funeraria Rosario: se dedica a ofrecer un servicio completo y compasivo en momentos de necesidad. 
        Con años de experiencia en el sector, nuestra misión es proporcionar apoyo integral a las familias 
        durante los momentos más difíciles, asegurando que cada detalle sea manejado con la máxima 
        sensibilidad y respeto.

        Nuestros Servicios Incluyen:
        1. Servicio de Cremación
        2. Servicio de Exhumacion
        3. Servicio de Entierro

        En Funeraria Rosario, entendemos que cada vida es única y que cada despedida debe reflejar ese valor. 
        Nos comprometemos a ofrecer un servicio personalizado que respete las tradiciones, creencias y 
        deseos de cada familia.

        Servicios particulares de la funeraria
        1. Finanzas
        2. Gestion de Inventario
    """

    label = tk.Label(ventanaDescripcion, text=texto, padx=10, pady=10, anchor="w", width=70, height=20, wraplength=480)
    label.pack(pady=15)

    btnContinuar = tk.Button(ventanaDescripcion, text="Continuar",
                                            command=lambda: ventanaDescripcion.destroy())
    btnContinuar.pack(pady=20)

    ventanaDescripcion.mainloop()

def ventanaPrincipal():
    global ventana 
    ventana = tk.Tk()
    ventana.geometry("600x400")
    ventana.title("Funeraria Rosario, su muerte mi slario")
    #Frame 2 - Zona 1 - Menus
    zona1=tk.Frame(ventana)
    zona1.pack(side="top",fill="x",anchor="nw",padx=2,pady=2)

    # Implementacion de las funcionalidades (Zona 2)
    zona2 = tk.Frame(ventana)
    zona2.pack(fill=tk.BOTH, expand=True)
    zona2.configure(bg="white")
    
    #MenuPrincipal
    menuPrincipal = tk.Menu(ventana)
    ventana.config(menu=menuPrincipal)

    #Menú archivo
    archivo=tk.Menu(menuPrincipal,tearoff=0)
   
    menuPrincipal.add_cascade(label="Archivo", menu=archivo)
    #Armar menú archivo
    archivo.add_command(label="Aplicación", command=aplicacion)
    archivo.add_separator()
    archivo.add_command(label="Salir", command=irVentanaInicio)
    
    #Menú procesos
    procesos=tk.Menu(menuPrincipal,tearoff=0)

    menuPrincipal.add_cascade(label="Procesos y consultas",menu=procesos)
    procesos.add_command(label="Cremación",command=lambda:cremacion.funcionalidadCrematorio(zona2))

    #Menú ayuda
    ayuda=tk.Menu(menuPrincipal,tearoff=0)

    menuPrincipal.add_cascade(label="Ayuda",menu=ayuda)


    



    #btnInicio=tk.Button(ventana,text="Regresar",command=irVentanaInicio)
    #btnInicio.pack(expand=True)
    #ventana.mainloop()