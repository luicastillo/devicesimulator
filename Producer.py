from msilib.schema import Class, File
from os import system
import time
import queue
import random
import logging
import json
from wsgiref.simple_server import make_server
from datetime import  datetime
from pip import main

class Producer:

    def __init__(self):
        self.id = 0
        self.cola = queue.Queue(maxsize=100)
        self.today = datetime.now()
        self.item = {}

    
    logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s',)

    def Generador (self):      
        while True: 
            if not self.cola.full():
                
                #creacion del id
                archivo = open('consecutivo.txt','r+')
                lista = []
                lista = list(archivo)
                ultvalor = len(lista)
                insertarint = int (lista[ultvalor-1]) + 1
                self.id = insertarint
                insertarstr = str (insertarint)
                archivo.write(insertarstr+'\n')

                self.item = {'id':self.id, 'timestamp':time.mktime(self.today.timetuple()), 'metric': random.randint(1, 100)}
                self.cola.put(self.item)
                logging.info(f'Nuevo elemento dentro de la cola {self.item}')
                time_to_sleep = random.randint(1, 3)
                time.sleep(time_to_sleep)

                return self.item

producer = Producer()



def application (environ, start_response):

    headers = [('Content-type','application/json')]
    start_response('200 OK',headers)
    return [bytes(json.dumps(producer.Generador()),'utf-8')]


if __name__=='__main__':

    servidor = make_server('localhost',8003,application)
    print("Serving on port 8003...")
    servidor.serve_forever()
    

