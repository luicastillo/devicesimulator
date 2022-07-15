# devicesimulator

# Diagrama de conexion microservicios: 

https://drive.google.com/file/d/1W2x-MG5P1SscvG_8_ZXe4cebR76_kMzW/view?usp=sharing

# Pasos instalacion y funcionaiento de los componentes

1) instalar motor de base de datos postgresql del siguiente link: https://www.postgresql.org/download/

2) Ejecutar comando: pip install psycopg2

3) Ejecutar comando: pip install  FastAPI


# Estando ubicado en la carpeta raiz del proyecto y desde consola de comandos, ejecutar:

1) py Producer.py

2) py Consumer.py

3) uvicorn crud:app --reload

4) curl http://localhost:8001 


Esto ultimo activa el get del cosumer hacia la cola del producer permitiendo ejecutar un menu de opciones del crud

#Menu de opciones:

Escoja lo que quiere hacer:

                        1) Visualizar
												
                        2) Guardar
												
                        3) Editar
												
                        4) Eliminar 
												
                        5) Salir del menu

