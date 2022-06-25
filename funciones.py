from datetime import datetime
import matplotlib.pyplot as plt

date = str(datetime.now())

año = int(date[:4])
mes = int(date[5:7])

def prueba():
    x = [1,2,3,4,5,6,7,8,9,10,11,12]
    y = [0, 30, 30, 25, 40, 50, 65, 30, 50, 65, 10, 14]

    plt.bar(x,y)
    plt.xlabel("Mes")
    plt.ylabel("Cantidad")
    plt.show()

prueba()

def incrementa(tipo, cantidad):
    """Incrementa la pieza 'tipo' en la base de datos."""
    #coger datos de la base de datos
    #sumar 1 a ese dato
    #meter el valor nuevo en la base de datos
    #actualizar la base de datos
    pass

def muestra (tipo, año):
    """Muestra estadísticas de la pieza seleccionada en el año seleccionado."""
    #coger de la base de datos de la pieza los datos de cada mes (está en un array 'Serie' en pandas)
    pass

