import random
import Lore

# Muodostaa yhdistyksen tietokantoihin
Yhdiste = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="Insert your database here",
    user="root",
    password="insert your password here",
    autocommit=True,
)
# Valitsee 15 satunaista lentokentää suomesta ja lajitelee ne aakosa järjestyksesttä

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
# tekee tehtäviä
def Tehtavat():
    sql = """SELECT * From goal;"""
    cursor = Yhdiste.cursor(dictionary=True)
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

# määritää pelääjalle tämän aloitus alkoholin(Alkoholia käytetään liikumiseen), pelaajan liikumus pituuden
def pelin_luonti(start_alcohol, lento_voima,Sijainti, nimi, kentat):
    sql="INSERT INTO game (alcohol,player_range,location,screen_name) VALUES (%s , %s , %s, %s);"
    cursor=Yhdiste.cursor(dictionary=True)
    cursor.execute(sql,(start_alcohol,lento_voima, Sijainti, nimi))

# Laitaa lentokentille joko: alkoholia,merkin taikka kelan
    tehtava= Tehtavat()
    lista= []
    for goal in tehtava:
        for i in range(0,goal['probability'], 1):
           lista.append(goal['id'])

    kentat = kentat[1:].copy()
    random.shuffle(kentat)


# antaa aloitus määrät eli. Pelaaja aloitaa pelin 1000L alkoholia, pelaaja pystyy liikumaan 2000? pelaaja aloittaa Helsinki vantaan lento kentällä. Pelaajan nimi on pakosta vaikka hän ei halua on Darrapukki.
pelin_luonti(1000, 2000, "EFHK", "Darrapukki")

