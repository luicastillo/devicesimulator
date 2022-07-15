from os import system
import threading
import requests
from wsgiref.simple_server import make_server
import json

def refresh():
    system('curl http://localhost:8003')

def consumer (environ, start_response):

    headers = [('Content-type','application/json')]
    start_response('200 OK',headers)

    url = 'http://localhost:8003/'
    urlpost = 'http://localhost:8000/post'
    urlput = 'http://localhost:8000/put'
    urlget = 'http://localhost:8000/get'


    response = requests.get(url)
    

    if response.status_code == 200:
        cadena = response.text
        cadenados = json.loads(cadena)

        enunciado = """ Escoja lo que quiere hacer:
                        1) Visualizar
                        2) Guardar
                        3) Editar
                        4) Eliminar 
                        5) Salir del menu
                        """
        print(enunciado)
        opcion = int(input())
        guardado = {'mensaje':'Guardado'}
        visor = {'mensaje':'visualizado'}
        eliminado = {'mensaje':'Eliminado'}
        actualizado = {'mensaje':'Actualizado'}

        if opcion == 1:
            requests.get(urlget)
            return [bytes(json.dumps(visor),'utf-8')]
        elif opcion == 2:
            requests.post(urlpost,data=json.dumps(cadenados))
            return [bytes(json.dumps(guardado),'utf-8')]
        elif opcion == 3:
            requests.put(urlput,data=json.dumps(cadenados))
            return [bytes(json.dumps(actualizado),'utf-8')]
        elif opcion == 4:
            requests.delete(urlput,data=json.dumps(cadenados))
            idd = input('Digite el id a borrar:')
            borrar = 'http://localhost:8000/delete/{}'.format(idd)
            requests.delete(borrar)
            return [bytes(json.dumps(eliminado),'utf-8')]

    elif response.status_code == 404:
        return print('Not Found.')

if __name__=='__main__':
    servidor = make_server('localhost',8001,consumer)
    print("Serving on port 8001...")
    servidor.serve_forever()

    refrescar = threading.Timer(10,refresh)
    refrescar.start()