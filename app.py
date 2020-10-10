from flask import Flask, jsonify, request
from poleas import seleccionar_poleas

app = Flask(__name__)


@app.route('/api')
def api():
    potencia_motor = request.args.get('potencia_motor')
    velocidad_polea_motora = request.args.get('velocidad_polea_motora')
    relac_transmision = request.args.get('relac_transmision')
    fact_servicio = request.args.get('fact_servicio')

    return jsonify(seleccionar_poleas(potencia_motor, velocidad_polea_motora, relac_transmision, fact_servicio))


if __name__ == '__main__':
    app.run(debug=True, port=4000)
