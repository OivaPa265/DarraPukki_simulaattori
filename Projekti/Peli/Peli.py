import random
import mysql.connector
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)


CORS(app)

CORS(app, resources={r"/*": {"origins": "*"}})


# Muodostaa yhdistyksen tietokantoihin
Yhdiste = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="demo",
    user="root",
    password="7523",
    autocommit=True,
)

# Valitsee 15 satunaista lentokentää suomesta ja lajitelee ne aakkos-järjestyksessä
def lokaatiot():
    sql ="""
SELECT * FROM(
SELECT iso_country, ident, name
FROM airport
WHERE iso_country ="FI"
ORDER by iso_country desc, rand()
LIMIT 15
) AS airports
ORDER BY name asc;"""
    cursor = Yhdiste.cursor(dictionary=True)
    cursor.execute(sql)
    return cursor.fetchall()

# tekee tehtäviä # no shit - ME 27/2/2026
def tehtavat():
    sql = "SELECT * From goal;"
    cursor = Yhdiste.cursor(dictionary=True)
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

# Määritää pelaajalle tämän aloitus alkoholin (Alkoholia käytetään liikumiseen), pelaajan liikumus pituuden
def pelin_luonti(alcohol, lento_voima, sijainti, nimi, kentat):
    cursor = Yhdiste.cursor(dictionary=True)
    sql = "INSERT INTO game (alcohol, player_range, location, screen_name) VALUES (%s, %s, %s, %s);"
    cursor.execute(sql, (alcohol, lento_voima, sijainti, nimi))
    peli_id = cursor.lastrowid  # Haetaan uuden pelin ID

    # Laitaa lentokentille joko: alkoholia, merkin, taikka kelan
    tehtava = tehtavat()
    lista = []
    for goal in tehtava:
        for i in range(0,goal['probability']):
            lista.append(goal['id'])

    # Sekoitaa kentät jokaisessa pelin alussa paitsi aloitus kenttä EFHK
    uusi_kentat = kentat[1:].copy()
    random.shuffle(uusi_kentat)

    # Laitaa tehtäviä
    for i, goal_id in enumerate(lista):
        if i < len(uusi_kentat): # tarkistaa ettei  Varmistetaan ettei kentät lopu kesken
            cursor = Yhdiste.cursor(dictionary=True)
            sql = "INSERT INTO ports (game, airport, goal) VALUES (%s, %s, %s);"
            cursor.execute(sql, (peli_id, uusi_kentat[i]['ident'], goal_id))
    return peli_id

# katsoo etäisyytä kenttien välillä
def get_airport_info(icao):

    sql = ("SELECT iso_country, ident, name, latitude_deg, longitude_deg "
           "FROM airport "
           "WHERE ident = %s")
    cursor = Yhdiste.cursor(dictionary=True)
    cursor.execute(sql, (icao,))
    return cursor.fetchall()

# tee kentän tarkistus jutska
# juu juu teen teen minä
def Kentan_tehtava(g_id, cur_airport):
    sql = f'''SELECT ports.id, goal, goal.id as goal_id, name, alcohol as money 
    FROM ports 
    JOIN goal ON goal.id = ports.goal 
    WHERE game = %s 
    AND airport = %s'''
    cursor = Yhdiste.cursor(dictionary=True)
    cursor.execute(sql, (g_id, cur_airport))
    result = cursor.fetchone()
    if result is None:
        return False
    return result

def Liikuminen(peli_id, target_icao):
    state = pelaajan_tavarat(peli_id)

    current_icao = state["location"]
    current_range = state["player_range"]
    current_alcohol = state["alcohol"]

    old_info = get_airport_info(current_icao)
    new_info = get_airport_info(target_icao)

    lat1, lon1 = old_info[0]['latitude_deg'], old_info[0]['longitude_deg']
    lat2, lon2 = new_info[0]['latitude_deg'], new_info[0]['longitude_deg']

    distance = int(((lat2-lat1)**2 + (lon2-lon1)**2)**0.5 * 300)

    if distance > current_range:
        return {"error": "LiianKaukana"}

    alcohol_used = max(200, int(distance / 10))
    new_alcohol = current_alcohol - alcohol_used

    cursor = Yhdiste.cursor(dictionary=True)
    sql = "UPDATE game SET location = %s, alcohol = %s WHERE id = %s"
    cursor.execute(sql, (target_icao, new_alcohol, peli_id))

    return {
        "message": "Liikui",
        "Matka": distance,
        "AlkoholiaJäljellä": new_alcohol
    }

# katsoo pelaajan tavarat ja sijainnin
def pelaajan_tavarat(peli_id):
    cursor = Yhdiste.cursor(dictionary=True)
    sql = "SELECT alcohol, player_range, location FROM game WHERE id = %s"
    cursor.execute(sql, (peli_id,))
    return cursor.fetchone()


@app.route("/start", methods=["POST"])
def Pelin_aloitus():
    data = request.json
    nimi = data.get("name", "Darrapukki")

    kentat = lokaatiot()
    peli_id = pelin_luonti(1000, 1000, "EFHK", nimi, kentat)

    return jsonify({"game_id": peli_id})


@app.route("/state/<int:peli_id>", methods=["GET"])
def state(peli_id):
    return jsonify(pelaajan_tavarat(peli_id))


@app.route('/airports', methods=['GET'])
def Hae_Kentat():
    data = lokaatiot()
    result = []
    for a in data:
        info = get_airport_info(a['ident'])
        if info:
            result.append(info[0])
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)
