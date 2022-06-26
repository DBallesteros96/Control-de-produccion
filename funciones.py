from datetime import datetime
import matplotlib.pyplot as plt
import datos, sqlite3, Interfaz

date = str(datetime.now())

año = int(date[:4])
mes = int(date[5:7])

def prueba():
    x = [1,2,3,4,5,6,7,8,9,10,11,12]
    y = [15, 30, 30, 25, 40, 50, 65, 30, 50, 65, 10, 14]

    plt.bar(x,y)
    plt.xlabel("Mes")
    plt.ylabel("Cantidad")
    plt.show()

def incrementa(tipo, cantidad):
    """Incrementa la pieza 'tipo' en la base de datos."""
    #coger datos de la base de datos
    #sumar 1 a ese dato
    #meter el valor nuevo en la base de datos
    #actualizar la base de datos
    pass

def muestra ():
    """Muestra estadísticas de la pieza seleccionada en el año seleccionado."""
    grafx = [1,2,3,4,5,6,7,8,9,10,11,12]
    grafy = []

    if Interfaz.seleccion[0] == 1:
        muelle = "RNM68"
    elif Interfaz.seleccion[0] == 2:
        muelle = "RNH68"
    elif Interfaz.seleccion[0] == 3:
        muelle = "RNH30"
    elif Interfaz.seleccion[0] == 4:
        muelle = "RNH25"

    if Interfaz.seleccion[1] == 1:
        periodo = 2022
    elif Interfaz.seleccion[1] == 2:
        periodo = 2023
    
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
    plt.show()


