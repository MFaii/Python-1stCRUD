# pip install mysql-connector-python
import mysql.connector

class CConexion:

  def ConexionBaseDeDatos():
    try:
      conexion = mysql.connector.connect(user='root',password='admin',host='127.0.0.1',database='clientesdb',port='3306')
      print("Conexion establecida")

      return conexion


    except mysql.connector.Error as error:
      print("Error al conectar a la base de datos {}".format(error))

      return conexion
    
  ConexionBaseDeDatos()