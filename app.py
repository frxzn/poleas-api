from flask import Flask, jsonify, request, Response
from poleas import seleccionar_poleas

app = Flask(__name__)


@app.route('/api')
def api():
    potencia_motor = request.args.get('potencia_motor')
    velocidad_polea_motora = request.args.get('velocidad_polea_motora')
    relac_transmision = request.args.get('relac_transmision')
    fact_servicio = request.args.get('fact_servicio')

    if potencia_motor and velocidad_polea_motora and relac_transmision and fact_servicio:
      return jsonify(seleccionar_poleas(potencia_motor, velocidad_polea_motora, relac_transmision, fact_servicio))
    else:
      return jsonify({"error": {"message": "Some variable missing", "status": 400}})


if __name__ == '__main__':
    app.run(debug=True, port=4000)
