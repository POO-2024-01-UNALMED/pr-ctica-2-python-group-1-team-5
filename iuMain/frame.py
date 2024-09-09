from tkinter import ttk, Label, Frame, Button
from iuMain.manejoErrores.errorAplicacion import ErrorAplicacion


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
            pass
        else:
            ErrorAplicacion("Debes completar todos los campos para poder continuar")

    def widget(self):
        for i,etiquetaFor in enumerate(self.etiquetas):
            etiqueta = Label(self.secundario, text=etiquetaFor)
            etiqueta.grid(row=i,column=0,padx=5,pady=5,sticky="e")
            self.etiquetasAlmacenadas.append(etiqueta) 
            opciones = ttk.Combobox(self.secundario, values=self.opciones[i])
            opciones.grid(row=i,column=1,padx=5,pady=5,sticky="w")
            self.opcionesAlmacenadas.append(opciones)
            
        btnContinuar=Button(self.secundario,text="Continuar", command=self.continuar)
        btnContinuar.grid(row=i+1,column=2,columnspan=2)
   
    def valoresIndices(self):
        listaIndices =[]
        for opcionSeleccionada in (self.opcionesAlmacenadas):
            eleccion = opcionSeleccionada.get()
            listaIndices.append(self.opciones.index(eleccion))
        return listaIndices
    

   