#Actividad 2
from tkinter import *
from tkinter import ttk


class Interfaz3:
    def __init__(self,raiz):
        raiz.title("Inicio de sesion")


        self.usuario = StringVar()
        self.contraseña =StringVar()


        mainFrame = ttk.Frame(raiz, padding=" 20 30 20 30", relief="raised", width=300, height=300) #el pading sirve para poder hacer una distancia del widget al panel. (izquierda arriba derecha abajo)
        mainFrame.grid(column=0, row=0, pady=25)

        subFrame = ttk.Frame(raiz, padding=" 65 30 65 30", relief="raised", width=300, height=300)
        subFrame.grid(column=0, row= 1)

        treeFrame = ttk.Frame(raiz, padding=" 20 30 20 30")
        treeFrame.grid(column=0, row=2)

        cuarFrame = ttk.Frame(raiz, padding=" 20 30 20 30")
        cuarFrame.grid(column=1, row=0)

        quinFrame = ttk.Frame(raiz, padding=" 20 30 20 30")
        quinFrame.grid(column=1, row=1)


        nombreEntry = ttk.Entry(mainFrame, width=35, textvariable=self.usuario)
        nombreEntry.grid(column=1, row=0)


        paternoEntry = ttk.Entry(mainFrame, width=35, textvariable=self.contraseña)
        paternoEntry.grid(column=1, row=2)

        maternoEntry = ttk.Entry(mainFrame, width=35, textvariable=self.usuario)
        maternoEntry.grid(column=1, row=4)

        correoEntry = ttk.Entry(mainFrame, width=35, textvariable=self.usuario)
        correoEntry.grid(column=1, row=6)

        movilEntry = ttk.Entry(mainFrame, width=35, textvariable=self.usuario)
        movilEntry.grid(column=1, row=8)

        #Datos frame 1

        ttk.Label(mainFrame, text="Nombre: ").grid(column=0, row=0,padx=15, pady=15) 
        ttk.Label(mainFrame, text="A. Paterno: ").grid(column=0, row=2,padx=15, pady=15) 
        ttk.Label(mainFrame, text="A. Materno: ").grid(column=0, row=4, padx=15,  pady=15) 
        ttk.Label(mainFrame, text="Correo: ").grid(column=0, row=6,padx=15, pady=15) 
        ttk.Label(mainFrame, text="Movil: ").grid(column=0, row=8,padx=15, pady=15) 

        #Botones Guardar y cancelar

        ttk.Button(treeFrame, text="Guardar").grid(column=0, row=15, padx=60) #boton 
        ttk.Button(treeFrame, text="Cancelar").grid(column=2, row=15,padx=60) #boton

        #Aficiones frame 2

        ttk.Label(subFrame, text="Aficiones: ").grid(column=1, row= 12, sticky=(W,S,N,E))
        ttk.Checkbutton(subFrame, text="Leer").grid(column=1, row= 13, padx=5)
        ttk.Checkbutton(subFrame, text="Musica").grid(column=2, row= 13,padx=5)
        ttk.Checkbutton(subFrame, text="Videojuegos").grid(column=3, row= 13, padx=5)
        

        #RadioButtons

        ttk.Radiobutton(cuarFrame, text="Estudiante").grid(column=3, row=5, sticky=(W,S,N,E))
        ttk.Radiobutton(cuarFrame, text="Empleado").grid(column=3, row=6, sticky=(W,S,N,E))
        ttk.Radiobutton(cuarFrame, text="Desempleado").grid(column=3, row=7, sticky=(W,S,N,E))

        #WIDGET ESTADOS LINEA DE ELECCION

        estado = StringVar()

        comboEstados = ttk.Combobox(quinFrame, text ="Estados(32)")
        comboEstados.grid(column=2, row=4, sticky=(W))
        comboEstados['values'] = ("Jalisco", "Nayarit", "Colima", "Colima", "Michoacan")

        raiz.mainloop()

        
        


    
