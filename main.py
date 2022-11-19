from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve


app=Flask(__name__)
cors = CORS(app)

from Controladores.ControladorMesa import ControladorMesa
miControladorMesa=ControladorMesa()

from Controladores.ControladorPartido import ControladorPartido
miControladorPartido = ControladorPartido



#Controlador Partido

@app.route("/partidos",methods=['GET'])
def getPartido():
    json=miControladorPartido.index()
    return jsonify(json)

@app.route("/partidos",methods=['POST'])
def crearPartidos():
    data = request.get_json()
    json=miControladorPartido.create(data)
    return jsonify(json)

@app.route("/partidos/<string:id>",methods=['GET'])
def getPartidos(id):
    json=miControladorPartido.show(id)
    return jsonify(json)

@app.route("/partidos/<string:id>",methods=['PUT'])
def modificarPartidos(id):
    data = request.get_json()
    json=miControladorPartido.update(id,data)
    return jsonify(json)

@app.route("/partidos/<string:id>",methods=['DELETE'])
def eliminarPartidos(id):
    json=miControladorPartido.delete(id)
    return jsonify(json)


#Controlador Mesa
@app.route("/",methods=['GET'])
def test():
    json = {}
    json["message"]="Server running ..."
    return jsonify(json)
@app.route("/mesas",methods=['GET'])
def getMesa():
    json=miControladorMesa.index()
    return jsonify(json)

@app.route("/mesas",methods=['POST'])
def crearMesas():
    data = request.get_json()
    json=miControladorMesa.create(data)
    return jsonify(json)

@app.route("/mesas/<string:id>",methods=['GET'])
def getMesas(id):
    json=miControladorMesa.show(id)
    return jsonify(json)

@app.route("/mesas/<string:id>",methods=['PUT'])
def modificarMesas(id):
    data = request.get_json()
    json=miControladorMesa.update(id,data)
    return jsonify(json)

@app.route("/mesas/<string:id>",methods=['DELETE'])
def eliminarMesas(id):
    json=miControladorMesa.delete(id)
    return jsonify(json)


#Controlador Candidato
@app.route("/candidatos",methods=['GET'])
def getCandidato():
    json=miControladorMesa.index()
    return jsonify(json)

@app.route("/candidatos",methods=['POST'])
def crearCandidato():
    data = request.get_json()
    json=miControladorMesa.create(data)
    return jsonify(json)

@app.route("/candidatos/<string:id>",methods=['GET'])
def getCandidatos(id):
    json=miControladorMesa.show(id)
    return jsonify(json)

@app.route("/candidatos/<string:id>",methods=['PUT'])
def modificarCandidato(id):
    data = request.get_json()
    json=miControladorMesa.update(id,data)
    return jsonify(json)

@app.route("/candidatos/<string:id>",methods=['DELETE'])
def eliminarCandidato(id):
    json=miControladorMesa.delete(id)
    return jsonify(json)


#Controlador Resultado
@app.route("/resultados",methods=['GET'])
def getResultado():
    json=miControladorMesa.index()
    return jsonify(json)

@app.route("/resultados",methods=['POST'])
def crearResultado():
    data = request.get_json()
    json=miControladorMesa.create(data)
    return jsonify(json)

@app.route("/resultados/<string:id>",methods=['GET'])
def getResultados(id):
    json=miControladorMesa.show(id)
    return jsonify(json)

@app.route("/resultados/<string:id>",methods=['PUT'])
def modificarResultado(id):
    data = request.get_json()
    json=miControladorMesa.update(id,data)
    return jsonify(json)

@app.route("/resultados/<string:id>",methods=['DELETE'])
def eliminarResultado(id):
    json=miControladorMesa.delete(id)
    return jsonify(json)

#Controladores
def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data

if __name__=='__main__':
    dataConfig = loadFileConfig()
    print("Server running : "+"http://"+dataConfig["url-backend"]+":" + str(dataConfig["port"]))
    serve(app,host=dataConfig["url-backend"],port=dataConfig["port"])

