#importando Flask
from flask import Flask, jsonify
from flask import request

#creando la instancia de FLask
app= Flask(__name__)

#configurar la application
app.config['DEBUG'] =True

# definiendo nuestra ruta principal
@app.route('/', methods= ['GET', 'POST', 'PUT', 'DELETE'])
def main():

    data = {
        "mensaje" : "hola mundo desde flask"
    }
    return jsonify(data), 200

#ruta con parametros en la url
@app.route('/users/<int:id>', methods= ['GET'])
def get_params_url(id):
    data = {
        "user" : id
    }
    return jsonify(data), 200

#definiendo una ruta con parametros a traves de query
#ejemplo: /users/?limit.   para esto necesitamos un objeto request

@app.route('/users', methods= ['GET'])
def get_params_query():
    params= request.args
    return jsonify(params), 200

# definiendo una rita con info en el body
# ejemplo: 'users/create'

@app.route('/users/create', methods = ['POST'])
def get_info_body():
    #recibir informacion
    info= request.data

    #recibir informacion formato json
    info= request.get_json()
    print(info["name"])
    print(info["lastname"])


    #recibir informacion en formato json y acceder a cada uno
    name= request.json.get("name")
    lastname= request.json.get("lastname")
    print(name)
    print(lastname)

    print(info)

    #recibir informacion formato formulario archivo opcional
    name= request.form["name"]
    lastname= request.form["lastname"]

    #recibir informacion en formato formulario, cuando son img or pdf, archivos en general
    file = request.files("cv")
    print(name)
    print(lastname)
    print(file.filename)
    return jsonify(info)


#iniciando nuestra applicacion
if __name__ == '__main__':
    app.run()