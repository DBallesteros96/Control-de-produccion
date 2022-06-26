import funciones
import sqlite3


#Cambiar las conexiones a la base de datos por un @decorador.

def crear_tabla():
    """Ejecutar una vez para la creación"""
    con = sqlite3.connect(".\datos\RNM68_2022")
    cur = con.cursor()
    cur.execute("""CREATE TABLE RNM68_2022 ('Mes' int, 'Cantidad' int)""")
    for x in range (1, 13):
        cur.execute("""INSERT INTO RNM68_2022 VALUES ({}, 0)""".format(x))
    con.commit()
    con.close()

def obtener_RNM68_2022():
    con = sqlite3.connect(".\datos\RNM68_2022")
    cur = con.cursor()
    cur.execute("""SELECT Cantidad FROM RNM68_2022 WHERE Mes = {}""".format(funciones.mes))
    cantidad = cur.fetchall()
    cantidad = int(cantidad[0][0])
    con.close()
    print (cantidad)

def insertar_RNM68_2022():
    con = sqlite3.connect(".\datos\RNM68_2022")
    cur = con.cursor()
    cur.execute("""SELECT Cantidad FROM RNM68_2022 WHERE Mes = {}""".format(funciones.mes))
    cantidad = cur.fetchall()
    cantidad = int(cantidad[0][0])
    cantidad += 1
    cur.execute("""UPDATE RNM68_2022 SET Cantidad = {} WHERE Mes = {}""".format(cantidad, funciones.mes))
    con.commit()
    con.close()

