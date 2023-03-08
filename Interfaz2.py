#Actividad 2
from tkinter import *
from tkinter import ttk


class Interfaz2:
    def __init__(self,raiz):
        raiz.title("Inicio de sesion")


        self.usuario = StringVar()
        self.contraseña =StringVar()


        mainFrame = ttk.Frame(raiz, padding=" 20 30 20 30") #el pading sirve para poder hacer una distancia del widget al panel. (izquierda arriba derecha abajo)
        mainFrame.grid(column=1, row=0)


        usuarioEntry = ttk.Entry(mainFrame, width=35, textvariable=self.usuario)
        usuarioEntry.grid(column=1, row=0)


        contraseñaEntry = ttk.Entry(mainFrame, width=35, textvariable=self.contraseña)
        contraseñaEntry.grid(column=1, row=2)






        ttk.Label(mainFrame, text="Usuario").grid(column=0, row=0, pady=15) #panel usuario
        ttk.Label(mainFrame, text="Contraseña ").grid(column=0, row=2, pady=15) #panel contraseña


        ttk.Button(mainFrame, text="Ingresar").grid(column=1, row=4, sticky=(E)) #boton
