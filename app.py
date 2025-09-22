from flask import Flask 
from flask import render_template
import sqlite3

app = Flask(__name__)

connection = sqlite3.connect ('my_database.db', check_same_thread=False)
cursor = connection.cursor()


def productDB():#возвращать данные по товарам
   listDB = cursor.execute('SELECT * FROM product')
   return listDB.fetchall()#возвращаем данные в виде list

@app.route('/')#главная страница
def index ():
    shop = productDB()
    return render_template ("index.html", shop = shop)

@app.route('/catalog')#каталог
def catalog ():
    return  render_template ("catalog.html")

@app.route('/T-shorts')#футболки
def Tshorts ():
    return  render_template ("T-short.html")

@app.route('/hoodie')#худи
def hoodie():
    return  render_template ("hoodie.html")

@app.route('/accessories')#худи
def accessories():
    return  render_template ("accessories.html")

if __name__ == '__main__':  #точка входа нашей программы
    app.run (debug=True)
