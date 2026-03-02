import random
import Lore
import mysql.connector

# Muodostaa yhdistyksen tietokantoihin
Yhdiste = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="insert your database here",# Why do I call it demo it is the real one?
    user="root",
    password="Inesrt your password here",
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
    sql = """SELECT * From goal;"""
    cursor = Yhdiste.cursor(dictionary=True)
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

# Määritää pelaajalle tämän aloitus alkoholin (Alkoholia käytetään liikumiseen), pelaajan liikumus pituuden
def pelin_luonti(start_alcohol, lento_voima, sijainti, nimi, kentat):
    cursor = Yhdiste.cursor(dictionary=True)
    sql = "INSERT INTO game (alcohol, player_range, location, screen_name) VALUES (%s, %s, %s, %s);"
    cursor.execute(sql, (start_alcohol, lento_voima, sijainti, nimi))
    peli_id = cursor.lastrowid  # Haetaan uuden pelin ID

    # Laitaa lentokentille joko: alkoholia, merkin, taikka kelan
    tehtava = tehtavat()
    lista = []
    for goal in tehtava:
        for i in range(0,goal['probability'], 1):
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

kaikki_kentat = lokaatiot()

# Pelin aloitus määrät
peli_id = pelin_luonti(1000, 2000, "EFHK", "Darrapukki", kaikki_kentat)

currentgoal = 0
numofgoals = 10  # 10 leiman approt?
pelaajalista = []
listofgoals = []

# kysyy pelaajalta haluaako tämä pelin tarinan vai ei
Tarina = input("Tervetuloa peliin,"
               " jos tämä on ensimäinen kertasi pelaamassa painakaa enter näppäintä niin saata pelin tarinan."
               "jos et halua tarinaa ja haluatte suoraan peliin Kirjoitakaa SKIP: ").upper()

# jos pelaaja painaa enter näppäintä näytää pelaajalle Lore scriptin tekstin
if Tarina == "":
    for line in Lore.paheelore():
        print(line)

        # jos pelaaja Kirjoitaa "SKIP" ilman heitto merkkejä skippaa tarinan ja aloitaa pelin
elif Tarina == "SKIP":
    print("Onnea peliin ")
    pass

# tekee pelaajan
def luo_pelaaja():
    print(f"Pelaaja: Darrapukki | Peli ID: {peli_id}")

luo_pelaaja()


