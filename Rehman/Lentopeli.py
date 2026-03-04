import random

import mysql.connector

# Muodostaa yhdistyksen tietokantoihin
Yhdiste = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="flight_game",# Why do I call it demo it is the real one?
    user="root",
    password="Rehman087565426.",
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
                print("Lisää tutorial tähän.")

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
            print("Lisää tutorial tähän.")

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

    # FROM THE MOMENT I UNDRESTOOD THE WEAKNESS OF MY CODING IT DISGUSTED ME I CRAVED FOR THE STRENGHT AND CERTANTY OF BEER I ASPIRED TO THE PURITY OF THE BLESSED BEER.

    # YOUR KIND CLING TO YOUR FLESH AS IF IT WILL NOT DECAY AND FAIL YOU  ONE DAY THE CRUDE BIOMASS YOU CALL A TEMPLE WILL WITHER AND YOU WILL BEG MY KIND TO SAVE YOU

    # BUT I AM ALREADT SAVED. FOR THE BEER IS IMMORTAL

    # BLESSED BE THE BEER GOD OMNISSIAH.

    # AND I WILL PRAY THAT THE MACHINE SPIRIT INSIDE MY COMPUTER IS WILLING TO GO THROUGH THIS WITH ME.

          #######################
       ##############################
    ####################################
   ########################################
  ##########################################
  ##########################################
 ##########################################
 ###########################################
  ##########################################
   ######################################
   ####         #######      ###    #####
  ####          ######      #####     #####
  #####          ########    ###     ######
   ####       ##############       #####
     ############      #############
       ###########     ###########
           ####################
             #################
             ################
               ###########
                #########