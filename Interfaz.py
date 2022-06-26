import tkinter as tk
import funciones
import datos

seleccion = []

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
                  font=('Helvetica', 18, "bold")).grid(row=0, column=0, padx=5, pady=5)
        #RNM68
        tk.Label(self, text="RNM68").grid(row=1, column=0)
        tk.Button(self, text="+1", background="#CECECE", height=2, width=2, command=datos.insertar_RNM68_2022).grid(row=1, column=1, padx=5, pady=5)
        #RNH68
        tk.Label(self, text="RNH68").grid(row=2, column=0)
        tk.Button(self, text="+1", background="#CECECE", height=2, width=2).grid(row=2, column=1, padx=5, pady=5)        
        #RNH25
        tk.Label(self, text="RNH25").grid(row=3, column=0)
        tk.Button(self, text="+1", background="#CECECE", height=2, width=2).grid(row=3, column=1, padx=5, pady=5)        
        #RNH30
        tk.Label(self, text="RNH30").grid(row=4, column=0)
        tk.Button(self, text="+1", background="#CECECE", height=2, width=2).grid(row=4, column=1, padx=5, pady=5)        

        tk.Button(self, text="Atrás", background="#CECECE",
                  command=lambda: master.switch_frame(Produccion)).grid(row=5, column=0, padx=5, pady=5)

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
                  font=('Helvetica', 18, "bold")).grid(row=0, column=0, padx=5, pady=5)
        tk.Button(self, text="Atrás", background="#CECECE",
                  command=lambda: master.switch_frame(Produccion)).grid(row=1, column=0, padx=5, pady=5)

class Estadisticas(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Estadísticas", font=('Helvetica', 18, "bold")).grid(row=0, column=0, padx=5, pady=5)
        tk.Button(self, text="Muelles", height=2, width=15, background="#CECECE",
                  command=lambda: master.switch_frame(Muelles_Stats)).grid(row=1, column=0, padx=5, pady=5)
        tk.Button(self, text="Labios", height=2, width=15, background="#CECECE",
                  command=lambda: master.switch_frame(Labios)).grid(row=2, column=0, padx=5, pady=5)
        tk.Button(self, text="Puertas", height=2, width=15, background="#CECECE",
                  command=lambda: master.switch_frame(Puertas)).grid(row=3, column=0, padx=5, pady=5)
        tk.Button(self, text="Volver a Inicio", background="#CECECE",
                  command=lambda: master.switch_frame(Inicio)).grid(row=4, column=0, padx=5, pady=5)

class Muelles_Stats(tk.Frame):
    def __init__(self, master):

        muelle_selec = tk.IntVar()
        año_selec = tk.IntVar()

        tk.Frame.__init__(self, master)

        tk.Label(self, text="Mecánicos").grid(row=0, column=0, padx=5, pady=5)
        tk.Radiobutton(self, text=("RNM68"), value=1, variable=muelle_selec).grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self, text=("Hidráulicos")).grid(row=1, column=0, padx=5, pady=5)
        tk.Radiobutton(self, text=("RNH68"), value=2, variable=muelle_selec).grid(row=1, column=1, padx=5, pady=5)
        tk.Radiobutton(self, text=("RNH30"), value=3, variable=muelle_selec).grid(row=2, column=1, padx=5, pady=5)
        tk.Radiobutton(self, text=("RNH25"), value=4, variable=muelle_selec).grid(row=3, column=1, padx=5, pady=5)

        tk.Label(self, text=("Año")).grid(row=4, column=0, padx=5, pady=5)
        tk.Radiobutton(self, text=("2022"), value=1, variable=año_selec).grid(row=4, column=1, padx=5, pady=5)
        tk.Radiobutton(self, text=("2023"), value=2, variable=año_selec).grid(row=4, column=2, padx=5, pady=5)

        tk.Button(self, text="Volver a Inicio", background="#CECECE",
                  command=lambda: master.switch_frame(Inicio)).grid(row=5, column=1, padx=5, pady=5)
        tk.Button(self, text="Estadísticas", background="#CECECE",
                  command=funciones.muestra).grid(row=5, column=2, padx=5, pady=5)

        seleccion.append(muelle_selec.get())
        seleccion.append(año_selec.get())

        print (seleccion)

if __name__ == "__main__":
    app = SampleApp()
    app.title("Control de Producción")
    app.grid_columnconfigure(0, weight=1)
    app.grid_rowconfigure(0, weight=1)
    app.geometry("350x300")
    app.mainloop()
    