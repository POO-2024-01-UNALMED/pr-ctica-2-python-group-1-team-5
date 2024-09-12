from tkinter import messagebox


class ErrorAplicacion(Exception):
    def __init__(self, mensaje):
        self._mensaje = f"Manejo de errores de la Aplicación\n{mensaje}"
        super().__init__(self._mensaje)
        self.enviarMensaje()

    def enviarMensaje(self):
        messagebox.showerror("Error", self._mensaje)

class CamposIncompletos(ErrorAplicacion):
    def __init__(self, mensaje):
        super().__init__(self._mensaje)
    
    def validacion():
        return False
    
class errorNumeros(ErrorAplicacion):
    def __init__(self, valor,mensaje,valMin=None,valMax=None):
        self.valor=valor
        self.vaMin=valMin
        self.valMax=valMax
        if valMin !=None and valMax !=None:
            self.topes()
        if valor.isdigit():
            super().__init__(mensaje)
        else:
             messagebox.showerror("Error", "Debes ingresar un dígito")
    
    def topes(self):
        pass