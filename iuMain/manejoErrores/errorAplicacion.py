from tkinter import messagebox


class ErrorAplicacion(Exception):
    def __init__(self, mensaje):
        self._mensaje = f"Manejo de errores de la Aplicación\n{mensaje}"
        super().__init__(self._mensaje)
        self.enviarMensaje()

    def enviarMensaje(self):
        messagebox.showerror("Error", self._mensaje)
