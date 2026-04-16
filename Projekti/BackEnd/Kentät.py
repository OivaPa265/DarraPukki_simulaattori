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

kaikki_kentat = lokaatiot()

sijainti= "EFHK"