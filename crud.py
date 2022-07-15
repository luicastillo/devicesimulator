from cmath import e
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Text
from uuid import uuid4 as uuid
import uvicorn
import psycopg2

class conexion_db:
  
  def __init__(self):
    self.conexion = psycopg2.connect(
      host="localhost",
      database="device",
      user="postgres",
      password="luis1992"
    )

    self.cursor = self.conexion.cursor()
    print('conexion establecida')
    
  def insert_db(self,idd,time,mtr):
    sentencia = "INSERT INTO metricas (idd,time_stamp,metrics) VALUES ('{}','{}','{}')".format(idd,time,mtr)
    try:
      self.cursor.execute(sentencia)
      self.conexion.commit()
      informe = 'se han insertado los datos: idd: {}, time_stamp: {}, metrics: {}'.format(idd,time,mtr)
      print(informe)

    except Exception as e:
      print('no se ha podido insertar: '+e)

  def update_db(self,idd,time,mtr):
    sentencia = "UPDATE metricas SET time_stamp = '{}', metrics = '{}' WHERE idd = '{}' ".format(time,mtr,idd)
    try:
      self.cursor.execute(sentencia)
      self.conexion.commit()
      informe = 'se han actualizado los datos: en idd: {} nuevo time_stamp: {}, nueva metrics: {}'.format(idd,time,mtr)
      print(informe)
    except Exception as e:
      print('no se ha dado la actualizacion de datos: '+e)
      raise

  def delete_db(self,idd):
    sentencia = "DELETE FROM metricas WHERE idd = '{}'".format(idd)
    try:
      self.cursor.execute(sentencia)
      self.conexion.commit()
      informe = 'se ha eliminado el id: {}'.format(idd)
      print(informe)
    except Exception as e:
      print('no se ha dado la elminacion de datos '+e)
      raise  

  def select_db(self):
    sentencia = "SELECT idd,time_stamp, metrics FROM metricas"
    try:
      self.cursor.execute(sentencia)
      metricas = self.cursor.fetchall()
      for metric in metricas:
        print("id: ",metric[0])
        print("timestamp: ",metric[1])
        print("metricas: ",metric[2])
        print("________________________\n")

      print('seleccion toda la tabla')
    except Exception as e:
      print('no se ha dado el select')
      raise
    


#iniciacion API
app = FastAPI()

#inicializamos conexion base de datos
db = conexion_db()

#declaramos el modelo del json que se recibe
class Modelo (BaseModel):
  id: str
  timestamp: str
  metric: str

@app.post('/post')
def request_post(post:Modelo):
  dato = post.dict()
  print (dato)
  db.insert_db(dato["id"],dato["timestamp"],dato["metric"])
  return 'dato insertado'

@app.put('/put')
def request_put(put:Modelo):                                      
  cid = input('Digite id a cambiar: ')
  ctimestamp = input('Digite nuevo valor timestamp: ')
  cmetric = input('Digite nuevo valor de metrica: ')
  db.update_db(cid,ctimestamp,cmetric)
  return 'update realizado realizada'

@app.delete('/delete/{post_id}')
def request_delete(post_id: str):
  db.delete_db(post_id)
  return 'dato borrado'

@app.get('/get')
def request_get():
  select = db.select_db()
  return select