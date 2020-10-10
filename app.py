from flask import Flask, jsonify, request, Response
from flask_cors import CORS, cross_origin
from poleas import seleccionar_poleas

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/api')
@cross_origin()
def api():
    potencia_motor = request.args.get('potencia_motor')
    velocidad_polea_motora = request.args.get('velocidad_polea_motora')
    relac_transmision = request.args.get('relac_transmision')
    fact_servicio = request.args.get('fact_servicio')

    if potencia_motor and velocidad_polea_motora and relac_transmision and fact_servicio:
      return jsonify(seleccionar_poleas(potencia_motor, velocidad_polea_motora, relac_transmision, fact_servicio))
    else:
      return Response('{"error": "Some variable missing"}', 400, mimetype='application/json')


if __name__ == '__main__':
    app.run(debug=True, port=4000)
