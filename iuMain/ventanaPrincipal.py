#Autores 
# Violeta Gomez
# Sebastian Guerra
# Andres Perez 

import tkinter as tk
from iuMain import ventanaInicio
from iuMain.funcionalidades import cremacion
from iuMain.funcionalidades import exhumacion
from iuMain.funcionalidades import entierro

from iuMain.funcionalidades import finanzas
from iuMain.funcionalidades import inventario

#Regresar a la ventana de inicio
def irVentanaInicio():
    ventana.destroy()
    ventanaInicio.ventanaInicio()


def framePrincipal(frame):
    #Organizacion del frame principal al entrar a la ventana principal
    for widget in frame.winfo_children():
        widget.destroy()
    
    etiquetaInicial = tk.Label(frame, 
                 text="Funeraria Rosario, su muerte mi salario",
                 bg="#92abc3",   # Color de fondo de la etiqueta
                 fg="#333333",   # Color del texto
                 font=("Helvetica", 16, "bold"),  # Tipo y tamaño de fuente
                 padx=10,        # Espacio interno horizontal
                 pady=10,        # Espacio interno vertical
                 relief="raised",  # Estilo del borde
                 borderwidth=2)  # Ancho del borde
    etiquetaInicial.pack(pady=10)

    tk.Label(frame,text="Lo invitamos a consultar nuestros servicios en el menú de Procesos y consultas",
                 bg="#8ad0b2",   # Color de fondo de la etiqueta
                 fg="#333333",   # Color del texto
                 font=("Helvetica", 16, "bold"),  # Tipo y tamaño de fuente
                 padx=10,        # Espacio interno horizontal
                 pady=10,        # Espacio interno vertical
                 relief="raised",  # Estilo del borde
                 borderwidth=2).pack(pady=6) 






def ayudaFunct():
    #mensaje que aparece al activar el botón de ayuda
    tk.messagebox.showinfo("Ayuda", "Nombres desarrolladores: \n-Violeta Gomez\n-Andres Perez\n-Sebastian Guerra")


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
    ventana.title("Funeraria Rosario, su muerte mi salario")
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
    procesos.add_separator()
    procesos.add_command(label="Exhumacion",command=lambda:exhumacion.funcionalidadExhumacion(zona2))
    procesos.add_separator()
    procesos.add_command(label="Entierro",command=lambda:entierro.funcionalidadEntierro(zona2))
    procesos.add_separator()
    procesos.add_command(label="Finanzas",command=lambda:finanzas.funcionalidadFinanzas(zona2))
    procesos.add_separator()
    procesos.add_command(label="Gestion de inventario",command=lambda:inventario.funcionalidadGestionInventario(zona2))

    #Menú ayuda
    ayuda=tk.Menu(menuPrincipal,tearoff=0)

    menuPrincipal.add_cascade(label="Ayuda",menu=ayuda)
    ayuda.add_command(label="Informacion",command=ayudaFunct)    

    framePrincipal(zona2)
