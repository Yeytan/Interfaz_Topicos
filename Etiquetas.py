from tkinter import *
from tkinter import ttk

raiz = Tk()
etqTexto = ttk.Label( raiz, text="Regular show Mordecai")#Tema interfaz
etqTexto.grid()

imagen = PhotoImage(file="regularshow.png")#Archivo

etqImagen = ttk.Label(raiz)
etqImagen.grid()
etqImagen ['image'] = imagen

etqCombinada = ttk.Label(raiz, text="Mordecai", compound= "top") #compund acomoda la imagen de acuerdo al texto.
etqCombinada.grid()
etqCombinada['image'] = imagen

raiz.mainloop()