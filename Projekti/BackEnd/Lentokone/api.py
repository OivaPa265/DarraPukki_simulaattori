from flask import Flask, request, jsonify
from flask_cors import CORS

import Peli

app = Flask(__name__)
CORS(app)

@app.route('/start_game', methods=['POST'])
def Pelin_aloitus():
    data = request.json
    kentat = Peli.lokaatiot()

    peli_id = Peli.pelin_luonti(
        data.get('alcohol', 1000),
        data.get('range', 1000),
        data.get('location', 'EFHK'),
        data.get('name', 'Player'),
        kentat
    )

    return jsonify({'peli_id': peli_id})


@app.route('/status/<int:peli_id>', methods=['GET'])
def status(peli_id):
    status = Peli.pelaajan_tavarat(peli_id)
    return jsonify(status)


@app.route('/move_player/<int:peli_id>', methods=['POST'])
def liikuminen(peli_id):
    data = request.json
    target_icao = data.get("new_icao")

    result = Peli.liikuminen(peli_id, target_icao)


    return jsonify(result)

@app.route('/airports', methods=['GET'])
def hae_kentat():
    data = Peli.lokaatiot()
    return jsonify(data)



if __name__ == '__main__':
    app.run(debug=True)