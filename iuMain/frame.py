#Autores 
# Violeta Gomez
# Sebastian Guerra


from tkinter import ttk, Label, Frame, Button, Entry
import tkinter as tk
from iuMain.manejoErrores.errorAplicacion import CamposIncompletos



"""
    Clase que crea un formulario con etiquetas y campos de entrada.
    Incluye un botón para resetear los valores de los campos.

    Attributes:
        master (tk.Widget): Widget contenedor principal.
        nombresEtiquetas (list of str): Lista de nombres para las etiquetas (no utilizada directamente).
        etiquetas (list of str): Lista de textos para las etiquetas.
        valores (list of str, optional): Valores predeterminados para los campos de entrada.
        editables (list of bool, optional): Estado de editabilidad de los campos de entrada.
"""

class FieldFrame(Frame):
    def __init__(self, master, nombresEtiquetas, etiquetas,valores=None, editables=None):
        super().__init__(master)
        self.frame = Frame(master)
        self.pack()
        self.nombresEtiquetas=nombresEtiquetas
        self.etiquetas=etiquetas
        self.valores=valores
        self.editables=editables
        self.btnBorrar=None

        # Asegurar que default_values, editables, y criteria_names sean listas
        if self.valores is None:
            self.valores = [''] * len(self.etiquetas)
        if self.editables is None:
            self.editables = [True] * len(self.etiquetas)

        self.entries = []
        self.secundario=Frame(self)
        self.secundario.pack()

        self.widget()


    def widget(self):
        #Crea y organiza las etiquetas y campos de entrada en el formulario.
        self.entries=[]
        # Crear etiquetas y cajas de texto
        for etiqueta, valor, editable in zip(self.etiquetas, self.valores, self.editables):
            entrada = Frame(self.secundario)
            label = Label(entrada, text=etiqueta)
            entry = Entry(entrada)
            
            # Configurar el valor por defecto
            entry.insert(0, valor)
            
            # Configurar si es editable o no
            entry.config(state=tk.NORMAL if editable else tk.DISABLED)
            
            # Organizar los widgets
            label.pack(side=tk.LEFT)
            entry.pack(side=tk.LEFT)
            
            # Añadir al contenedor de entradas
            self.entries.append(entry)
                        
            # Empaquetar el frame de cada entrada
            entrada.pack(padx=5, pady=5, fill=tk.X)
        
        self.btnBorrar = tk.Button(self.secundario, text="Borrar", command=self.borrar)
        self.btnBorrar.pack(side=tk.LEFT, padx=5)
        
        #button_frame.pack(pady=(5, 10))
    
    def bloquear(self):
        # Cambiar el estado de todas las entradas a 'disabled'
        for entrada in self.entries:
            entrada.config(state=tk.DISABLED)
        if self.btnBorrar:
            self.btnBorrar.destroy()
    
    def getValores(self):
        #retorna los indices de las variables
        valores = [entrada.get() for entrada in self.entries]
        return valores
    
    def borrar(self):
        #Borra todos los campos del formulario
        for entrada, valor in zip(self.entries, self.valores):
            entrada.config(state=tk.NORMAL)
            entrada.delete(0, tk.END)
            entrada.insert(0, valor)
            entrada.config(state=tk.NORMAL if entrada.cget('state') == tk.NORMAL else tk.DISABLED)
    
    def continuar(self,mensaje=""):
        # Verifica que todos los campos no estén vacíos
        for entrada in self.entries:
            if entrada.get().strip() == '':
                CamposIncompletos(mensaje)
                return False
        return True
    

"""
    Clase que crea un formulario con etiquetas y comboboxes (menús desplegables).

    Attributes:
        master (tk.Widget): Widget contenedor principal.
        etiquetas (list of str): Lista de textos para las etiquetas.
        opciones (list of list of str): Opciones disponibles para cada combobox.
"""


class frame1(Frame):
    def __init__(self, master, etiquetas, opciones):
        super().__init__(master)
        self.pack()  # Usa pack para el Frame principal

        self.master=master
        self.etiquetas=etiquetas
        self.opciones=opciones
        self.opcionesAlmacenadas = []
        self.etiquetasAlmacenadas = []

        self.secundario = Frame(self)
        self.secundario.grid(row=0, column=0)

        self.widget()
        

    def continuar(self,mensaje="faltante"):
        seleccionados = all(combobox.get() for combobox in self.opcionesAlmacenadas)
        if seleccionados:
            return True
        else:
            CamposIncompletos(mensaje)
            return False

    def widget(self):
        #Crea y organiza las etiquetas y comboboxes en el formulario.
        
        for i,etiquetaFor in enumerate(self.etiquetas):
            etiqueta = Label(self.secundario, text=etiquetaFor)
            etiqueta.grid(row=i,column=0,padx=5,pady=5,sticky="e")
            self.etiquetasAlmacenadas.append(etiqueta) 
            opciones = ttk.Combobox(self.secundario, values=self.opciones[i], state="readonly",width=30)
            opciones.grid(row=i,column=1,padx=5,pady=5,sticky="w")
            self.opcionesAlmacenadas.append(opciones)
            
        #btnContinuar=Button(self.secundario,text="Continuar", command=self.continuar)
        #btnContinuar.grid(row=i+1,column=2,columnspan=2)
   
    def getValores(self):
        listaIndices =[]
        if self.continuar():
            for i,opcionSeleccionada in enumerate(self.opcionesAlmacenadas):
                eleccion = opcionSeleccionada.current()
                listaIndices.append(eleccion)
        return listaIndices
    
    def bloquearOpciones(self):
        #Bloquea las opciones del combobox
        for opcion in self.opcionesAlmacenadas:
            opcion.config(state='disabled')

    def desbloquearOpciones(self):
        #Desbloquea las opciones del combobox
        for opcion in self.opcionesAlmacenadas:
            opcion.config(state="normal")

"""
    Clase que muestra una tabla con encabezados y valores.

    Attributes:
        master (tk.Widget): Widget contenedor principal.
        etiquetas (list of str): Lista de encabezados de columna.
        valores (list of list of str): Valores a mostrar en la tabla.
"""
    
class tablas(Frame):
    def __init__(self,master,etiquetas, valores):
        
        super().__init__(master)
        self.pack()
        self.etiquetas=etiquetas
        self.valores=valores

        self.secundario = Frame(self)
        self.secundario.grid(row=0, column=0)
        self.widget()
    
    def widget(self):
        # Crear encabezados de columna
        for i, c in enumerate(self.etiquetas):
            etiqueta = Label(self.secundario, text=c,borderwidth=2, relief="solid", width=12, height=1, bg="lightgray", font=('Helvetica', 11, 'bold'))
            etiqueta.grid(row=i,column=0,padx=2,pady=3)

        # Crear filas de valores
        for a, fila in enumerate(self.valores):
            for i, valor in enumerate(fila):
                valor_label = Label(self.secundario, text=valor, borderwidth=1, relief="solid", width=25, height=1)
                valor_label.grid(row=a, column=i+1, padx=2, pady=1)

 
