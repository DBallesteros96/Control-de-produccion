from datetime import datetime
import matplotlib.pyplot as plt
import datos, sqlite3, Interfaz
import tkinter as tk
import tkinter.messagebox

date = str(datetime.now())

año = int(date[:4])
mes = int(date[5:7])

def muestra (tipo_selec, año_selec):
    """Muestra estadísticas de la pieza seleccionada en el año seleccionado."""
    grafx = [1,2,3,4,5,6,7,8,9,10,11,12]
    grafy = []

    if tipo_selec == 1:
        tipo = "RNM68"
    elif tipo_selec == 2:
        tipo = "RNH68"
    elif tipo_selec == 3:
        tipo = "RNH30"
    elif tipo_selec == 4:
        tipo = "RNH25"
    elif tipo_selec == 5:
        tipo = "PInd800"
    elif tipo_selec == 6:
        tipo = "LNM6"
    elif tipo_selec == 7:
        tipo = "LNH25"
    elif tipo_selec == "LNH30":
        tipo = "LNH30"
    else:
        tk.messagebox.showerror("Error", "Seleccione una pieza.")

    if año_selec == 1:
        periodo = 2022
    elif año_selec == 2:
        periodo = 2023
    else:
        tk.messagebox.showinfo("Info", "Ningún año seleccionado. Se mostrará el año actual.")
        periodo = año
    
    con = sqlite3.connect(".\datos\{}_{}".format(tipo, periodo))
    cur = con.cursor()
    cur.execute("""SELECT Cantidad FROM {}_{}""".format(tipo, periodo))
    cantidad = cur.fetchall()
    for x in range (12):
        grafy.append(cantidad[x][0])
    con.close()

    plt.bar(grafx, grafy)
    plt.xlabel("Mes")
    plt.ylabel("Cantidad")
    plt.title("Producción {} {}".format(tipo, periodo))
    plt.show()


