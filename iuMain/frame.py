from tkinter import ttk, Label, Frame, Button, Entry
import tkinter as tk
from iuMain.manejoErrores.errorAplicacion import ErrorAplicacion


class FieldFrame(Frame):
    def __init__(self, master, nombresEtiquetas, etiquetas,valores=None, editables=None):
        super().__init__(master)
        self.frame = Frame(master)
        self.pack()
        self.nombresEtiquetas=nombresEtiquetas
        self.etiquetas=etiquetas
        self.valores=valores
        self.editables=editables

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
        
        btnBorrar = tk.Button(self.secundario, text="Borrar", command=self.borrar)
        btnBorrar.pack(side=tk.LEFT, padx=5)
        
        #button_frame.pack(pady=(5, 10))
    
    def getValores(self):
        return [entrada.get() for entrada in self.entries]
    
    def borrar(self):
        for entrada, valor in zip(self.entries, self.valores):
            entrada.config(state=tk.NORMAL)
            entrada.delete(0, tk.END)
            entrada.insert(0, valor)
            entrada.config(state=tk.NORMAL if entrada.cget('state') == tk.NORMAL else tk.DISABLED)
    def continuar(self):
        # Verifica que todos los campos no estén vacíos
        for entrada in self.entries:
            if entrada.get().strip() == '':
                ErrorAplicacion("Debes completar todos los campos para poder continuar")
                return False
        return True


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
        #btnContinuar=Button()
    def continuar(self):
        seleccionados = all(combobox.get() for combobox in self.opcionesAlmacenadas)
        if seleccionados:
            return True
        else:
            ErrorAplicacion("Debes completar todos los campos para poder continuar")
            return False

    def widget(self):
        for i,etiquetaFor in enumerate(self.etiquetas):
            etiqueta = Label(self.secundario, text=etiquetaFor)
            etiqueta.grid(row=i,column=0,padx=5,pady=5,sticky="e")
            self.etiquetasAlmacenadas.append(etiqueta) 
            opciones = ttk.Combobox(self.secundario, values=self.opciones[i])
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
            etiqueta = Label(self.secundario, text=c,borderwidth=2, relief="solid", width=13, height=2, bg="lightgray", font=('Helvetica', 11, 'bold'))
            etiqueta.grid(row=i,column=0,padx=2,pady=3)

        # Crear filas de valores
        for a, fila in enumerate(self.valores):
            for i, valor in enumerate(fila):
                valor_label = Label(self.secundario, text=valor, borderwidth=1, relief="solid", width=15, height=2)
                valor_label.grid(row=a, column=i+1, padx=2, pady=1)

 
