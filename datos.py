import funciones
import sqlite3

#Cambiar las conexiones a la base de datos por un @decorador.

def crear_tabla():
    """Ejecutar una vez para la creación"""
    con = sqlite3.connect(".\datos\LNH30_2023")
    cur = con.cursor()
    cur.execute("""CREATE TABLE LNH30_2023 ('Mes' int, 'Cantidad' int)""")
    for x in range (1, 13):
        cur.execute("""INSERT INTO LNH30_2023 VALUES ({}, 0)""".format(x))
    con.commit()
    con.close()

#crear_tabla()

#Muelles
def obtener_muelle(tipo, año):
    con = sqlite3.connect(".\datos\{}_{}".format(tipo, año))
    cur = con.cursor()
    cur.execute("""SELECT Cantidad FROM {}_{} WHERE Mes = {}""".format(tipo, año, funciones.mes))
    cantidad = cur.fetchall()
    cantidad = int(cantidad[0][0])
    con.close()
    return cantidad

def insertar_muelle(tipo, año):
    con = sqlite3.connect(".\datos\{}_{}".format(tipo, año))
    cur = con.cursor()
    cur.execute("""SELECT Cantidad FROM {}_{} WHERE Mes = {}""".format(tipo, año, funciones.mes))
    cantidad = cur.fetchall()
    cantidad = int(cantidad[0][0])
    cantidad += 1
    cur.execute("""UPDATE {}_{} SET Cantidad = {} WHERE Mes = {}""".format(tipo, año, cantidad, funciones.mes))
    con.commit()
    con.close()

#Puertas
def obtener_puerta(año):
    con = sqlite3.connect(".\datos\PInd800_{}".format(año))
    cur = con.cursor()
    cur.execute("""SELECT Cantidad FROM PInd800_{} WHERE Mes = {}""".format(año, funciones.mes))
    cantidad = cur.fetchall()
    cantidad = int(cantidad[0][0])
    con.close()
    return cantidad

def insertar_puerta(año, cant):
    con = sqlite3.connect(".\datos\PInd800_{}".format(año))
    cur = con.cursor()
    cur.execute("""SELECT Cantidad FROM PInd800_{} WHERE Mes = {}""".format(año, funciones.mes))
    cantidad = cur.fetchall()
    cantidad = int(cantidad[0][0])
    cantidad += cant
    cur.execute("""UPDATE PInd800_{} SET Cantidad = {} WHERE Mes = {}""".format(año, cantidad, funciones.mes))
    con.commit()
    con.close()

def obtener_labio(tipo, año, cant):
    con = sqlite3.connect(".\datos\{}_{}".format(tipo, año))
    cur = con.cursor()
    cur.execute("""SELECT Cantidad FROM {}_{} WHERE Mes = {}""".format(tipo, año, funciones.mes))
    cantidad = cur.fetchall()
    cantidad = int(cantidad[0][0])
    con.close()
    return cantidad


def insertar_labio(tipo, año, cant):
    con = sqlite3.connect(".\datos\{}_{}".format(tipo, año))
    cur = con.cursor()
    cur.execute("""SELECT Cantidad FROM {}_{} WHERE Mes = {}""".format(tipo, año, funciones.mes))
    cantidad = cur.fetchall()
    cantidad = int(cantidad[0][0])
    cantidad += cant
    cur.execute("""UPDATE {}_{} SET Cantidad = {} WHERE Mes = {}""".format(tipo, año, cantidad, funciones.mes))
    con.commit()
    con.close()



