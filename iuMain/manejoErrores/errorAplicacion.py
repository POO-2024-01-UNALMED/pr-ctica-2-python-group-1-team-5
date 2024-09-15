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
        self._mensaje=mensaje
        super().__init__(f"Campos incompletos {self._mensaje}")




    
class errorNumeros(ErrorAplicacion):
    def __init__(self, mensaje):
       
        self._mensaje = mensaje
        self._verificar = True
        super().__init__(f"Error números {mensaje}")

    def numeroEntero(self,valor):
        try:
            int(valor)
        except ValueError:
            # Actualiza el mensaje de error y relanza la excepción
            raise ErrorAplicacion("Debes ingresar un dígito")
        
    
    def numeroFloat(self,valor):
        try:
            float(valor)
        except ValueError:
            # Actualiza el mensaje de error y relanza la excepción
            raise ErrorAplicacion("Debes ingresar un dígito")

class errorIds(errorNumeros):
    def __init__(self, valor, mensaje=None, valMin=0, valMax=0):
        self.numeroEntero(valor)
          # Inicializa la clase base
          # Verifica si el valor es un número
        
        # Verifica si el valor es mayor o igual al valor mínimo
        if int(valor)<valMin:
            raise super().__init__("El número ingresado es menor al valor mínimo")
        elif int(valor)>valMax:
            raise super().__init__("El número ingresado es mayor al valor máximo")
        else:
            super().__init__(mensaje)
            

class errorPeso(errorNumeros):
     def __init__(self, valor,pesoMax,pesoMin=0):
        self.numeroFloat(valor)

        # Verifica si el valor es mayor o igual al valor mínimo
        if float(valor)<pesoMin or float(valor)>pesoMax:
            raise super().__init__("El valor del peso del cliente no es correcto")



class errorEstatura(errorNumeros):
     def __init__(self, valor,estaturaMax,estaturaMin=0):
        self.numeroFloat(valor)

        # Verifica si el valor es mayor o igual al valor mínimo
        if float(valor)<estaturaMin or float(valor)>estaturaMax:
            raise super().__init__("El valor de la estatura del cliente no es correcta")

        


    
    