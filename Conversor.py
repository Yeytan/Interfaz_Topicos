#Conversor de pies a metros


from tkinter import *
from tkinter import ttk


class Conversor:
    def __init__(self,raiz):
        raiz.title("Pies a Metros")


        self.pies = StringVar()
        self.metros=StringVar()


        mainFrame = ttk.Frame(raiz, padding=" 3 10 3 3") #el pading sirve para poder hacer una distancia del widget al panel. (izquierda arriba derecha abajo)
        mainFrame.grid(column=0, row=0)


        piesEntry = ttk.Entry(mainFrame, width=7, textvariable=self.pies)
        piesEntry.grid(column=1, row=0)


        ttk.Label(mainFrame, text="Pies").grid(column=2, row=0)#El sticky sirve para poder mover el widget en la orientacion deseada.
        ttk.Label(mainFrame, text="Equivalen a: ").grid(column=0, row=1)
        ttk.Label(mainFrame, textvariable=self.metros).grid(column=1, row=1)
        ttk.Label(mainFrame, text="Metros").grid(column=2, row=1)
        ttk.Button(mainFrame, text="Calcular", command=self.calcular).grid(column=2, row=2)


        piesEntry.focus()
        raiz.bind("<Return>", self.calcular)


    def calcular(self, *args):
        print("Boton presionado. ")
        pieUsuario = self.pies.get()
        print("Pies ingresados: ",pieUsuario)


        try:
            piesFlotante = float(pieUsuario)
            metros= piesFlotante*.3048
            print("metros: ", metros)
            self.metros.set(metros)
        except ValueError:
            print("No es un dato valido. ")


           




if __name__=="main_":
    print("Este es el archivo principal.")
    print("Nada mas se mostrara esto si es el prinipal.")
