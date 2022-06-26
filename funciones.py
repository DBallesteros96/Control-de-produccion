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

def hola():
    print(Interfaz.Muelles_Stats.muelle_selec)
    print ("Texto de prueba")

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
    plt.show()


