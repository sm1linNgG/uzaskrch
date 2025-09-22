import sqlite3

#создаем подключеник к базе даных (файл называевается "my_database.bd")
connection = sqlite3.connect('my_database.db')

#закрытие базы даных
connection.close()

#создаем подключение мк базе данных
connection = sqlite3.connect ('my_database.db')
cursor = connection.cursor()

def productDB():#возвращать данные по товарам
   listDB = cursor.execute('SELECT * FROM product')
   return listDB.fetchall()#возвращаем данные в виде list

if __name__ =='__main__':
   print(productDB())

