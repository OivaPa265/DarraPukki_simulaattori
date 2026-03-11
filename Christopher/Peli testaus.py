import random

import mysql.connector

# Muodostaa yhdistyksen tietokantoihin
Yhdiste = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="lisää sun database tähän",
    user="root",
    password="lisää sun salasana tähän",
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

# WHAT THE FUCK DID I WRITE WHY DOSE IT ONLY WORK WHEN LATITUDE AND LONGITUDE ARE THERE THEY NOT
def get_airport_info(icao):

    sql = ("SELECT iso_country, ident, name, latitude_deg, longitude_deg "
           "FROM airport "
           "WHERE ident = %s")
    cursor = Yhdiste.cursor(dictionary=True)
    cursor.execute(sql, (icao,))
    return cursor.fetchall()

kaikki_kentat = lokaatiot()

sijainti= "EFHK"

# Pelin aloitus määrät
peli_id = pelin_luonti(1000, 2000, "EFHK", "Darrapukki", kaikki_kentat)

currentgoal = 0
numofgoals = 10  # 10 leiman approt?
pelaajalista = []
listofgoals = []

# kysyy pelaajalta haluaako tämä pelin tarinan vai ei
def tarina():
    while True:
        print("" + "=" * 30)
        print("TERVETULOA PELIIN ")
        print( "Jos haluat tarinan paina enter, ")
        print(" jos haluat vain tutorialin kirjoita tutorial, ")
        print(" jos haluat suoraan peliin kirjoita skip :) ")
        print("" + "=" * 30)
        syote = input("Päätös tähän :").upper()

        # jos pelaaja painaa enter antaa tarinan
        print("" + "=" * 30)
        if syote == "":
            print("Tarinamme alkaa 2026 metropoliassa johon on tullut uusi opiskelija. Mutta tämä opiskelija ei ole vain kuka vaan vaan tämä on JOULUPUKKI\n"
         "JOULUPUKKI on päättänyt että hän ei jaksa opiskella vaan haluaa saada kaikista eniten merkkejä hänen haalareihinsa.\n"
         "Mutta pukki ei saa paljastaa että hän on pukki joten hänen on pitänyt löytää uusi tapa matkustaa ympäri suomea merkkejä keräämiseen\n"
         "Pukki päätti käytää hänen taikavoimiaan ja oppi lentämään alkoholin avulla \n")
            print("" + "=" * 30)

            # kysyy tarinan jälkeen jos pelaaja haluaan tutorialin
            uudeleen_kys = input("Haluatko tutorialin Y/N? ").upper()

            # jos painoi Y antaa tutorialin
            if uudeleen_kys == "Y":
                print("Tätä keskeneräistä peliä pelaat näppäimistöllä.\n"
                      "Sinulle näytetään lista 15 erilaisesta suomen lentokentistä joista valitset mihin haluat mennä\n"
                      "kun olet valinnut haluamasi kentän kirjoita kentän numero ja paina enter näppäintä\n"
                      "Tehtäväsi on kerätä x määrä merkkejä")

                # jos painoi N aloitaa pelin
            elif uudeleen_kys == "N":
                print("Onnea peliin :)")
                break
            print("" + "=" * 30)
            # kysyy pelaajalta jos hän ymmärsi
            ymmarsiko = input("Ymmärsitkö Y/N? ").upper()

            #jos painoi Y aloitaa pelin
            print("" + "=" * 30)
            if ymmarsiko == "Y":
                print("Hyvä sillä mä en")

                break

                # jos painoi N naytää uudestaan
            else:
                print("Ole tarkkana tällä kertaa")
                continue

        # jos pelaaja kirjoitti pass antaa tutorialin

        elif syote == "TUTORIAL":
            print("" + "=" * 30)
            print("Tätä keskeneräistä peliä pelaat näppäimistöllä.\n"
                      "Sinulle näytetään lista 15 erilaisesta suomen lentokentistä joista valitset mihin haluat mennä\n"
                      "kun olet valinnut haluamasi kentän kirjoita kentän numero ja paina enter näppäintä\n"
                      "Tehtäväsi on kerätä x määrä merkkejä")

        # kysyy jos ymmmärsi
            print("" + "=" * 30)
            ymmarsiko_2 = input("Ymmärsitkö Y/N? ").upper()
            # jos kirjoitaa Y aloitaa pelin
            if ymmarsiko_2 == "Y":
                print("Hyvä sillä mä en")
                break

                # jos kirjoitti N näyttää uudestaan
            else:
                print("Ole tarkkana tällä kertaa")
                continue

            # jos pelaaja kirjoitti skip aloitaa pelin suoraan
        elif syote == "SKIP":
            print("Onnea peliin :)")
            break

tarina()

def pelaajan_tavarat(peli_id):
    cursor = Yhdiste.cursor(dictionary=True)
    # katto missä pelaaja on
    sql = "SELECT alcohol, player_range, location FROM game WHERE id = %s"
    cursor.execute(sql, (peli_id,))
    return cursor.fetchone()

hävijö = False
voitto = False

# PERKELE TÄMÄ ON SE PELI
while not hävijö:
    # Katoo pelaajan vitun lokaation alkohlin ja liikumis matkan pelissä. eipä vielkää pysty liiku eikö vain hä mikset sä tehnyt sitä hä hä miks sä teit tän hä et sit saanu sitä toimii nii joo muute mitä mun piti ees tehä vittu mä en muista ei helvetti mä en muista miks mä teen tätä 12 aamulla miksne mä tehnyt tätä aikasemmi voi vittu siihen on vaa 9 päivää ei vitttuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu
    tavarat = pelaajan_tavarat(peli_id)
    # määritää paskat pelaajalle
    current_alcohol = tavarat['alcohol']
    current_range = tavarat['player_range']
    current_icao = tavarat['location']

    # hakee jotai vittu
    kentta_info = get_airport_info(current_icao)
    kentta_nimi = kentta_info[0]['name']

    # tekee ihan VITUN hienon näytö pelaajalle siitä missä hän on VITTU MÄ OON YLPEE TÄST
    print("" + "=" * 30)
    print(f" |ALOITUS | DARRAPUKKI SIMULAATORI ID| {peli_id}" "")
    print(f" |SIJAINTI| {kentta_nimi} ({current_icao})")
    print(f" |ALKOHOLI| {current_alcohol}ml")
    print(f" |LIIKUMIS| {current_range}m")
    print("=" * 30)

    # ei tee mitää
    input(" TEE SIIRTYMINEN SEURAAVAKSI ")
    break

 
import random
import sys

# Tässä Funktio laskee kahden pisteen välisen etäisyyden
def appropiste(piste1, piste2):
    if piste1 > piste2:              # Tarkistaa kumpi pisteistä on suurempi
        erotus = piste1 - piste2     # Laskee pisteiden välinen erotus
    else:
        erotus = piste2 - piste1     # Eli jos piste2 on suurempi niin lasketaan näin
    return erotus   # Palauttaa lasketun etäisyyden


#Arvotaan eka piste väliltä 1000-10000
appropiste1 = random.randint(1000,10000)

#Arvotaan toka piste väliltä 1000-1000
appropiste2 = random.randint(1000,10000)

#Tulostetaan pisteet
print(appropiste1)
print(appropiste2)

# Kutsutaan funktiota ja tallenetaan tulosta muuttujaan, joka on matka.
matka = appropiste(appropiste1, appropiste2)

#Tulostetaan pisteiden  välinen etäisyys
print("Erotus on", matka)



# Teen koodi, kun sulla on 10 haalrimerrki, antaa erikois haalarinmerkkin

# Esim print sulla on 10/10 tässä sulle erikoismerkki

# Kuinka paljon alkoholi kuluu per metri, Alkoholi 1 Litra per Kilometri

kulutus = 1000

#Funktio laskee alkoholin kulutuksen
def kulutus(matka):
    litrat = matka/ 1000
    return litrat

tulos = kulutus(matka)


print("Alkoholia kuluu", tulos,"litraa")



# ----------------- ohjelma alkaa tästä ---------------------

def pelaajan_liike():
    alkoholi_ml = alkoholi * 1000
    if alkoholi_ml > matka:
        print("Vrummm vrummm vrummm lennetään seuraavalle pisteelle")
    elif alkoholi_ml < matka:
        print("Bisse loppu et voi enää liikkua joten hävisit!")
        sys.exit()
    # pelaaja liikkuu jotenkin perkele
    return

#def polttoaine_negatiivinen():
    print("===============================================")
    print("Hävisit pelin koska olet niin huono juomaan!!! ")
    print("===============================================")
    return


#def polttoaine_liikaa():
    if alkoholi > 13:
        print("===================================")
        print("Hävisit pelin koska olet juoppo!!! ")
        print("===================================")
    # pelaaja taas vittu häivää koska se on vitun juoppo
    return

def voitto():
    print("==================================================================")
    print("Jeee voitit sait kaikki haalarimerkit tässä on erikois apro merkki")
    print("==================================================================")
    # Kun pelaaja kerää kaikki haalarimerkit se voittaa ja tähän tulee koodi voitto ruudulle
    return


def lista_lukumaara():
    pituus = len(haalarimerkit_lista)
    if pituus == 10:
        voitto()
    return pituus

def uusiyritys():
    return alkoholi

# -- Pääohjelma --

alkoholi = random.randint(0,10)
haalarimerkit_lista = []



while alkoholi > 0:
    print("=========================================")
    haalarimerkki = input("Keräätkö haalarimerkin? (paina Enter) ")
    # polttoaine_positiivinen()
    if haalarimerkki == "":
        print("- - - - - - - - - - - - - - - - - - - - -")
        print("Haalarimerkki löydetty!")
        print("- - - - - - - - - - - - - - - - - - - - -")
        haalarimerkit_lista.append(haalarimerkki)
        print("Sinulla on haalarimerkkejä tällä hetkellä",len(haalarimerkit_lista))
        lkm = lista_lukumaara()
        if lkm == 10:
            break
    print("=========================================")
    juo = input("Kaadanko kurkustasi bisseä? (paina Enter)")
    if juo == "":
        alkoholi = random.randint(0,26)
        print("- - - - - - - - - - - - - - - - - - - - -")
        print(f"Kaadoin kurkustasi alas {alkoholi} juomaa! ")
        print("- - - - - - - - - - - - - - - - - - - - -")
        pelaajan_liike()
