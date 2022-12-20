from flask import Blueprint, request, jsonify
import pyodbc

database = Blueprint("database", __name__, url_prefix="/database")


@database.route("/num_of_clients/", methods=['GET'])
def num_of_clients():
    access_driver = "DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\\Users\\Pasha\\Desktop\\Projects\\TestProject\\db.accdb"
    cnxm = pyodbc.connect(access_driver)
    cursor = cnxm.cursor()
    table_list = list(cursor.tables())

    cursor.execute('select COUNT(*) from "Клиент"')

    for row in cursor.fetchall():
        return str(row[0])


@database.route("/num_of_categories/", methods=['GET'])
def num_of_categories():
    access_driver = "DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\\Users\\Pasha\\Desktop\\Projects\\TestProject\\db.accdb"
    cnxm = pyodbc.connect(access_driver)
    cursor = cnxm.cursor()
    table_list = list(cursor.tables())

    cursor.execute('SELECT count(*) FROM "Категория"')

    for row in cursor.fetchall():
        return str(row[0])

@database.route("/num_of_positions/", methods=['GET'])
def num_of_positions():
    access_driver = "DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\\Users\\Pasha\\Desktop\\Projects\\TestProject\\db.accdb"
    cnxm = pyodbc.connect(access_driver)
    cursor = cnxm.cursor()
    table_list = list(cursor.tables())

    cursor.execute('SELECT count(*) FROM "Склад"')

    for row in cursor.fetchall():
        return str(row[0])






