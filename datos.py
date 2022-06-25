import funciones
import sqlite3

def crear_tabla():
    """Ejecutar una vez para la creación"""
    con = sqlite3.connect(".\datos\RNM68_2022")
    cur = con.cursor()
    cur.execute("""CREATE TABLE RNM68_2022 ('Mes' int, 'Cantidad' int)""")
    for x in range (1, 13):
        cur.execute("""INSERT INTO RNM68_2022 VALUES ({}, 0)""".format(x))
    con.commit()
    con.close()

#ERROR
def prueba():
    con = sqlite3.connect(".\datos\RNM68_2022")
    cur = con.cursor()
    cur.execute("""UPDATE RNM68_2022 SET Cantidad = {} WHERE Mes = {}""".format(7, funciones.mes))
    con.commit()
    con.close()

prueba()

#crear_tabla()
