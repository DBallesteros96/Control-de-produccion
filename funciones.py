from datetime import datetime
import matplotlib.pyplot as plt
import datos, sqlite3, Interfaz

date = str(datetime.now())

año = int(date[:4])
mes = int(date[5:7])

def muestra (tipo_selec, año_selec):
    """Muestra estadísticas de la pieza seleccionada en el año seleccionado."""
    grafx = [1,2,3,4,5,6,7,8,9,10,11,12]
    grafy = []


    if tipo_selec == 1:
        muelle = "RNM68"
    elif tipo_selec == 2:
        muelle = "RNH68"
    elif tipo_selec == 3:
        muelle = "RNH30"
    elif tipo_selec == 4:
        muelle = "RNH25"
    else:
        muelle = "RNM68"
    

    if año_selec == 1:
        periodo = 2022
    elif año_selec == 2:
        periodo = 2023
    else:
        periodo = año
    
    con = sqlite3.connect(".\datos\{}_{}".format(muelle, periodo))
    cur = con.cursor()
    cur.execute("""SELECT Cantidad FROM {}_{}""".format(muelle, periodo))
    cantidad = cur.fetchall()
    for x in range (12):
        grafy.append(cantidad[x][0])
    con.close()

    plt.bar(grafx, grafy)
    plt.xlabel("Mes")
    plt.ylabel("Cantidad")
    plt.title("Producción {} {}".format(muelle, periodo))
    plt.show()


