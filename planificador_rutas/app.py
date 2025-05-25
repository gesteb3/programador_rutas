from flask import Flask, render_template, request
from dijkstra import Paquete, Mapa

app = Flask(__name__)
mapa = Mapa()
paquetes = []

@app.route('/')
def index():
    return render_template("index.html", paquetes=paquetes)

@app.route('/agregar_paquete', methods=['POST'])
def agregar_paquete():
    destino = request.form['destino']
    lat = float(request.form['lat'])
    lon = float(request.form['lon'])
    paquete = Paquete(destino, lat, lon)
    paquetes.append(paquete)
    mapa.agregar_nodo(destino, lat, lon)
    return render_template("index.html", paquetes=paquetes, mensaje="Paquete agregado")

@app.route('/agregar_ruta', methods=['POST'])
def agregar_ruta():
    origen = request.form['origen']
    destino = request.form['destino']
    peso = float(request.form['peso'])
    mapa.agregar_arista(origen, destino, peso)
    return render_template("index.html", paquetes=paquetes, mensaje="Ruta agregada")

@app.route('/calcular_ruta', methods=['POST'])
def calcular_ruta():
    origen = request.form['inicio']
    destino = request.form['fin']
    try:
        ruta, costo = mapa.calcular_ruta(origen, destino)
        return render_template("index.html", paquetes=paquetes, ruta=ruta, costo=costo)
    except Exception as e:
        return render_template("index.html", paquetes=paquetes, error=str(e))

if __name__ == '__main__':
    app.run(debug=True)
