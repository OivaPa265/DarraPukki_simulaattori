import random
import Lore
import mysql.connector

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
    sql = """
SELECT * FROM(
SELECT iso_country, ident, name
FROM airport
WHERE iso_country ="FI"
ORDER by iso_country desc, rand()
LIMIT 15
) AS airports
ORDER BY name asc;"""
    cursor=Yhdiste.cursor(dictionary=True)
    cursor.execute(sql)
    result=cursor.fetchall()
    return result

# Tekee tehtäviä
def tehtavat():
    sql = """SELECT * From goal;"""
    cursor = Yhdiste.cursor(dictionary=True)
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

# Määritää pelaajalle tämän aloitus alkoholin(Alkoholia käytetään liikumiseen), pelaajan liikumus pituuden
def pelin_luonti(start_alcohol, lento_voima,sijainti, nimi, kentat):
    sql="INSERT INTO game (alcohol,player_range,location,screen_name) VALUES (%s , %s , %s, %s);"
    cursor=Yhdiste.cursor(dictionary=True)
    cursor.execute(sql,(start_alcohol,lento_voima, sijainti, nimi))
    peli_nimi = cursor.lastrowid



# Laitaa lentokentille joko: alkoholia, merkin, taikka kelan
    tehtava= tehtavat()
    lista= []
    for goal in tehtava:
        for i in range(0,goal['probability'], 1):
           lista.append(goal['id'])

    uusi_kentat = kentat[1:].copy()
    random.shuffle(kentat)

    for i, goal_id in enumerate (lista):
        if i <len(uusi_kentat):
         sql = "INSERT INTO ports (game, airport, goal) VALUES (%s, %s, %s);"
        cursor = Yhdiste.cursor(dictionary=True)
        cursor.execute(sql,(peli_nimi, tehtava[i]['ident'], goal_id))
    return peli_nimi


# Antaa aloitusmäärät eli. Pelaaja aloitaa pelin 1000L alkoholia, pelaaja pystyy liikumaan 2000? pelaaja aloittaa Helsinki-Vantaan lentokentällä. Pelaajan nimi on pakosta Darrapukki vaikka hän ei sitä itse halua.
pelin_luonti(1000, 2000, "EFHK", "Darrapukki", 10)

currentgoal = 0
numofgoals = 10  # 10 leiman approt?
pelaajalista = []
listofgoals = []


def luo_pelaaja():
    print("jotai hienoo tähä")
    pelaajalista.append(pelaaja)



