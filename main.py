from flask import Flask
##Requiest recibir parametros json 
from flask import request
from CRUD import Registros

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Este es mi main !'

@app.route("/Grabar", methods=['POST'])
def GrabarNuevosDatos():
    request_data = request.get_json(force=True)
    Nombre = request_data['Nombre']
    password = request_data['password']
    Registros.GrabarJson(Nombre,password)
    return '''
        El Nombre es: {}
        El Contraseña  es: {} '''.format(Nombre, password)

if __name__ == '__main__':
    app.run() 