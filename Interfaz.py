import tkinter as tk
import funciones
import datos
import tkinter.messagebox

def seleccionar():
    tipo = tipo_selec.get()
    año = año_selec.get()

class Seleccionar():
    tipo = 0
    año = 0

    def exe(self):
        Seleccionar.tipo = tipo_selec.get()
        Seleccionar.año = año_selec.get()

class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(Inicio)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.grid()

class Inicio(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Inicio", font=('Helvetica', 18, "bold")).grid(row=0, column=0, padx=5, pady=5)
        tk.Button(self, text="Producción", height=3, width=20, background="#CECECE",
                  command=lambda: master.switch_frame(Produccion)).grid(row=1, column=0, padx=5, pady=5)
        tk.Button(self, text="Estadísticas", height=3, width=20, background="#CECECE",
                  command=lambda: master.switch_frame(Estadisticas)).grid(row=2, column=0, padx=5, pady=5)

class Produccion(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="PRODUCCIÓN", font=('Helvetica', 18, "bold")).grid(row=0, column=0, padx=5, pady=5)
        tk.Button(self, text="Muelles", height=2, width=15, background="#CECECE",
                  command=lambda: master.switch_frame(Muelles)).grid(row=1, column=0, padx=5, pady=5)
        tk.Button(self, text="Labios", height=2, width=15, background="#CECECE",
                  command=lambda: master.switch_frame(Labios)).grid(row=2, column=0, padx=5, pady=5)
        tk.Button(self, text="Puertas", height=2, width=15, background="#CECECE",
                  command=lambda: master.switch_frame(Puertas)).grid(row=3, column=0, padx=5, pady=5)
        tk.Button(self, text="Volver a Inicio", background="#CECECE",
                  command=lambda: master.switch_frame(Inicio)).grid(row=4, column=0, padx=5, pady=5)

class Muelles(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Producción Muelles", 
                  font=('Helvetica', 18, "bold")).grid(row=0, column=1, padx=5, pady=5)
        #RNM68
        tk.Label(self, text="RNM68").grid(row=1, column=0)
        tk.Button(self, text="+1", background="#CECECE", height=2, width=2,
                  command=lambda: [datos.insertar_muelle("RNM68", funciones.año), self.actualiza_etiqueta("RNM68", 1)]).grid(row=1, column=1, padx=5, pady=5)
        tk.Label(self, text="Muelles RNM68 el mes {} del {} = {}".format(funciones.mes, funciones.año ,datos.obtener_muelle("RNM68", funciones.año))).grid(row=1, column=2)
        #RNH68
        tk.Label(self, text="RNH68").grid(row=2, column=0)
        tk.Button(self, text="+1", background="#CECECE", height=2, width=2,
                  command=lambda: [datos.insertar_muelle("RNH68", funciones.año), self.actualiza_etiqueta("RNH68", 2)]).grid(row=2, column=1, padx=5, pady=5)        
        tk.Label(self, text="Muelles RNH68 el mes {} del {} = {}".format(funciones.mes, funciones.año ,datos.obtener_muelle("RNH68", funciones.año))).grid(row=2, column=2)
        #RNH30
        tk.Label(self, text="RNH30").grid(row=3, column=0)
        tk.Button(self, text="+1", background="#CECECE", height=2, width=2,
                  command=lambda: [datos.insertar_muelle("RNH30", funciones.año), self.actualiza_etiqueta("RNH30", 3)]).grid(row=3, column=1, padx=5, pady=5)             
        tk.Label(self, text="Muelles RNH30 el mes {} del {} = {}".format(funciones.mes, funciones.año ,datos.obtener_muelle("RNH30", funciones.año))).grid(row=3, column=2)
        #RNH25
        tk.Label(self, text="RNH25").grid(row=4, column=0)
        tk.Button(self, text="+1", background="#CECECE", height=2, width=2, 
                  command=lambda: [datos.insertar_muelle("RNH25", funciones.año), self.actualiza_etiqueta("RNH25", 4)]).grid(row=4, column=1, padx=5, pady=5)        
        tk.Label(self, text="Muelles RNH25 el mes {} del {} = {}".format(funciones.mes, funciones.año, 
                  datos.obtener_muelle("RNH25", funciones.año))).grid(row=4, column=2)
        tk.Button(self, text="Atrás", background="#CECECE",
                  command=lambda: master.switch_frame(Produccion)).grid(row=5, column=1, padx=5, pady=5)
    
    def actualiza_etiqueta(self, muelle,  fila):
        tk.Label(self, text="Muelles {} el mes {} del {} = {}".format(muelle, funciones.mes, funciones.año, datos.obtener_muelle(muelle, funciones.año))).grid(row=fila, column=2)

class Labios(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Producción Labios",  
                  font=('Helvetica', 18, "bold")).grid(row=0, column=0, padx=5, pady=5)
        tk.Button(self, text="Atrás", background="#CECECE",
                  command=lambda: master.switch_frame(Produccion)).grid(row=1, column=0, padx=5, pady=5)

class Puertas(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Producción Puertas",
                  font=('Helvetica', 18, "bold")).grid(row=0, column=1, padx=5, pady=5)
        tk.Label(self, text="PInd800").grid(row=1, column=0, padx=5, pady=5)
        self.entrada = tk.Entry(self)
        self.entrada.insert(0, "Cantidad...")
        self.entrada.grid(row=1, column=1, padx=5, pady=5)
        tk.Button(self, text="Añadir", command= self.prueba_muestra_entry).grid(row=1, column=2, padx=5, pady=5)
        tk.Button(self, text="Atrás", background="#CECECE",
                  command=lambda: master.switch_frame(Produccion)).grid(row=2, column=1, padx=5, pady=5)

    def prueba_muestra_entry(self):
        cant = self.entrada.get()
        try:
           cant = int (cant)
        except:
            tk.messagebox.showerror("Error", "Introduzca un dato válido.")
        else:
            tk.messagebox.showinfo("Base de datos actualizada", 
            "{} puertas PInd800 añadidas a la base de datos".format(cant))
            datos.insertar_puerta(funciones.año, cant)

class Estadisticas(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Estadísticas", font=('Helvetica', 18, "bold")).grid(row=0, column=0, padx=5, pady=5)
        tk.Button(self, text="Muelles", height=2, width=15, background="#CECECE",
                  command=lambda: master.switch_frame(Muelles_Stats)).grid(row=1, column=0, padx=5, pady=5)
        tk.Button(self, text="Labios", height=2, width=15, background="#CECECE",
                  command=lambda: master.switch_frame(Labios)).grid(row=2, column=0, padx=5, pady=5)
        tk.Button(self, text="Puertas", height=2, width=15, background="#CECECE",
                  command=lambda: master.switch_frame(Puertas_Stats)).grid(row=3, column=0, padx=5, pady=5)
        tk.Button(self, text="Volver a Inicio", background="#CECECE",
                  command=lambda: master.switch_frame(Inicio)).grid(row=4, column=0, padx=5, pady=5)

class Muelles_Stats(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        tk.Label(self, text="Estadísticas Muelles",
                font=('Helvetica', 18, "bold")).grid(row=0, column=1, padx=5, pady=5)
        tk.Label(self, text="Mecánicos").grid(row=1, column=0, padx=5, pady=5)
        tk.Radiobutton(self, text=("RNM68"), value=1, variable=tipo_selec, command=seleccionar).grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self, text=("Hidráulicos")).grid(row=2, column=0, padx=5, pady=5)
        tk.Radiobutton(self, text=("RNH68"), value=2, variable=tipo_selec, command=seleccionar).grid(row=2, column=1, padx=5, pady=5)
        tk.Radiobutton(self, text=("RNH30"), value=3, variable=tipo_selec, command=seleccionar).grid(row=3, column=1, padx=5, pady=5)
        tk.Radiobutton(self, text=("RNH25"), value=4, variable=tipo_selec, command=seleccionar).grid(row=3, column=1, padx=5, pady=5)

        tk.Label(self, text=("Año")).grid(row=4, column=0, padx=5, pady=5)
        tk.Radiobutton(self, text=("2022"), value=1, variable=año_selec, command=seleccionar).grid(row=4, column=1, padx=5, pady=5)
        tk.Radiobutton(self, text=("2023"), value=2, variable=año_selec, command=seleccionar).grid(row=4, column=2, padx=5, pady=5)

        tk.Button(self, text="Volver a Inicio", background="#CECECE",
                  command=lambda: master.switch_frame(Inicio)).grid(row=6, column=1, padx=5, pady=5)
        tk.Button(self, text="Estadísticas", background="#CECECE",
                  command= lambda: funciones.muestra(tipo_selec.get(), año_selec.get())).grid(row=6, column=2, padx=5, pady=5)

class Puertas_Stats(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        tk.Label(self, text="Estadísticas Puertas",
                font=('Helvetica', 18, "bold")).grid(row=0, column=1, padx=5, pady=5)
        tk.Radiobutton(self, text=("PInd800"), value=5, variable=tipo_selec, command=seleccionar).grid(row=1, column=1, padx=5, pady=5)
        tk.Button(self, text="Volver a Inicio", background="#CECECE",
                  command=lambda: master.switch_frame(Inicio)).grid(row=3, column=1, padx=5, pady=5)
        tk.Button(self, text="Estadísticas", background="#CECECE", 
                  command= lambda: funciones.muestra(tipo_selec.get(), año_selec.get())).grid(row=3, column=2, padx=5, pady=5)
        tk.Label(self, text=("Año")).grid(row=2, column=0, padx=5, pady=5)
        tk.Radiobutton(self, text=("2022"), value=1, variable=año_selec, command=seleccionar).grid(row=2, column=1, padx=5, pady=5)
        tk.Radiobutton(self, text=("2023"), value=2, variable=año_selec, command=seleccionar).grid(row=2, column=2, padx=5, pady=5)


if __name__ == "__main__":
    app = SampleApp()

    tipo_selec = tk.IntVar()
    año_selec = tk.IntVar()

    app.title("Control de Producción")
    app.grid_columnconfigure(0, weight=1)
    app.grid_rowconfigure(0, weight=1)
    app.geometry("600x500")
    app.mainloop()
    