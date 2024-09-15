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
    def __init__(self, mensaje):
       
        self._mensaje = mensaje
        self._verificar = True
        super().__init__(mensaje)

    def numeroEntero(self,valor):
        try:
            int(valor)
        except ValueError:
            # Actualiza el mensaje de error y relanza la excepción
            raise ValueError("Debes ingresar un dígito") from None
    
    def numeroFloat(self,valor,mensaje):
        try:
            float(valor)
        except ValueError:
            # Actualiza el mensaje de error y relanza la excepción
            raise ValueError("Debes ingresar un dígito") from None

class errorIds(errorNumeros):
    def __init__(self, valor, mensaje=None, valMin=0, valMax=None):
        self.numeroEntero(valor)
        super().__init__(mensaje)  # Inicializa la clase base
          # Verifica si el valor es un número
        
        # Verifica si el valor es mayor o igual al valor mínimo
        if int(valor) >= valMin:
            self._mensaje = mensaje if mensaje else "El valor es válido."
        else:
            self._mensaje = "El número ingresado es menor al valor mínimo"
            raise ValueError(self._mensaje)

class errorPeso(errorNumeros):
     def __init__(self, valor):
        self.numeroFloat(valor)
        super().__init__("El valor del peso del cliente no es correcto")

class errorEstatura(errorNumeros):
     def __init__(self, valor):
        self.numeroFloat(valor)
        super().__init__("El valor de la estatura del cliente no es correcta")
        

        
"""
class errorNumeros(ErrorAplicacion):
    def __init__(self, valor,mensaje):
        self._valor=valor
        self._mensaje=mensaje
        self._verificar=True
        super().__init__(mensaje)

    def numero(self):
        try:
            int(self._valor)
        except:
            super().__init__("Debes ingresar un dígito")
            raise

class errorIds(errorNumeros):
    def __init__(self, valor,mensaje=None,valMin=0,valMax=0):
        self.numero()
        if int(valor)>=valMin:
            super().__init__(valor,mensaje)
        else:
            super().__init__(valor,"El número ingresado es menor al valor mínimo")

            """


    
    