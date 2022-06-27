import funciones
import sqlite3

#Cambiar las conexiones a la base de datos por un @decorador.

def crear_tabla():
    """Ejecutar una vez para la creación"""
    con = sqlite3.connect(".\datos\RNH25_2022")
    cur = con.cursor()
    cur.execute("""CREATE TABLE RNH25_2022 ('Mes' int, 'Cantidad' int)""")
    for x in range (1, 13):
        cur.execute("""INSERT INTO RNH25_2022 VALUES ({}, 0)""".format(x))
    con.commit()
    con.close()


def obtener(tipo, año):
    con = sqlite3.connect(".\datos\{}_{}".format(tipo, año))
    cur = con.cursor()
    cur.execute("""SELECT Cantidad FROM {}_{} WHERE Mes = {}""".format(tipo, año, funciones.mes))
    cantidad = cur.fetchall()
    cantidad = int(cantidad[0][0])
    con.close()
    return cantidad

def insertar(tipo, año):
    con = sqlite3.connect(".\datos\{}_{}".format(tipo, año))
    cur = con.cursor()
    cur.execute("""SELECT Cantidad FROM {}_{} WHERE Mes = {}""".format(tipo, año, funciones.mes))
    cantidad = cur.fetchall()
    cantidad = int(cantidad[0][0])
    cantidad += 1
    cur.execute("""UPDATE {}_{} SET Cantidad = {} WHERE Mes = {}""".format(tipo, año, cantidad, funciones.mes))
    con.commit()
    con.close()

