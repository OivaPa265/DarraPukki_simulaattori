import random
import mysql.connector
import miniPelit.Noppa
import miniPelit.BlackJack

# Muodostaa yhdistyksen tietokantoihin
Yhdiste = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="demo",# Why do I call it demo it is the real one?
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

kaikki_kentat = lokaatiot()

sijainti= "EFHK"

# Pelin aloitus määrät
peli_id = pelin_luonti(1000, 1000, "EFHK", "Darrapukki", kaikki_kentat)

currentgoal = 0
numofgoals = 3  # 10 leiman approt?
pelaajalista = []
listofgoals = []

# kysyy pelaajalta haluaako tämä pelin tarinan vai ei
def tarina():
    while True:
        print("" + "=" * 30)
        print("TERVETULOA PELIIN ")
        print( "Jos haluat tarinan paina enter, ")
        print( "jos haluat vain tutorialin kirjoita tutorial, ")
        print( "jos haluat suoraan peliin kirjoita skip :) ")
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
            uudeleen_kys = input("Haluatko tutorialin kyllä/ei? ").upper()




            # jos painoi Y antaa tutorialin
            if uudeleen_kys == "KYLLÄ":
                print("Tätä keskeneräistä peliä pelaat näppäimistöllä.\n"
                      "Sinulle näytetään lista 15 erilaisesta suomen lentokentistä joista valitset mihin haluat mennä\n"
                      "kun olet valinnut haluamasi kentän kirjoita kentän numero ja paina enter näppäintä\n"
                      "Tehtäväsi on kerätä x määrä merkkejä")

                # jos kirjoitti EI
            elif uudeleen_kys == "EI":
                print("Onnea peliin :)")
                break
            print("" + "=" * 30)
            # kysyy pelaajalta jos hän ymmärsi
            ymmarsiko = input("Ymmärsitkö Kyllä/ei? ").upper()

            #jos kirjoitti KYLLÄ
            print("" + "=" * 30)
            if ymmarsiko == "KYLLÄ":
                print("Hyvä sillä mä en")

                break

                # jos KIRJOITTI KYLLÄ
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
            ymmarsiko_2 = input("Ymmärsitkö Kyllä/Ei? ").upper()
            # jos kirjoitaa Y aloitaa pelin
            if ymmarsiko_2 == "KYLLÄ":
                print("Hyvä sillä mä en")
                break

                # jos kirjoitti EI
            else:
                print("Ole tarkkana tällä kertaa")
                continue

            # jos pelaaja kirjoitti skip aloitaa pelin suoraan
        elif syote == "SKIP":
            print("Onnea peliin :)")
            break

tarina()
# katsoo pelaajan tavarat ja sijainnin
def pelaajan_tavarat(peli_id):
    cursor = Yhdiste.cursor(dictionary=True)
    # katto missä pelaaja on
    sql = "SELECT alcohol, player_range, location FROM game WHERE id = %s"
    cursor.execute(sql, (peli_id,))
    return cursor.fetchone()

# määritää hävijön sekä voiton tavoitteet
hävijö = False
voitto = False

# itse peli WOW
while not hävijö:
    # Katoo pelaajan vitun lokaation alkohlin ja liikumis matkan pelissä. eipä vielkää pysty liiku eikö vain hä mikset sä tehnyt sitä hä hä miks sä teit tän hä et sit saanu sitä toimii nii joo muute mitä mun piti ees tehä vittu mä en muista ei helvetti mä en muista miks mä teen tätä 12 aamulla miksne mä tehnyt tätä aikasemmi voi vittu siihen on vaa 9 päivää ei vitttuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu
    tavarat = pelaajan_tavarat(peli_id)
    # määritää paskat pelaajalle
    current_alcohol = tavarat['alcohol']
    current_range = tavarat['player_range']
    current_icao = tavarat['location']

   # hakee pelaajan sijainnin
    kentta_info = get_airport_info(current_icao)
    kentta_nimi = kentta_info[0]['name']

    # printaa pelaajalle tämän: nimen, nykyisen kentän, alkolohin määrän ja liikumis pituuden
    print("" + "=" * 30)
    print(f" |ALOITUS | DARRAPUKKI SIMULAATORI |ID| {peli_id}" "")
    print(f" |SIJAINTI| {kentta_nimi} ({current_icao})")
    print(f" |ALKOHOLI| {current_alcohol}ml")
    print(f" |LIIKUMIS| {current_range}m")
    print (f" |MERKKI|   {currentgoal}/{numofgoals}")
    print("=" * 30)


    # katoo jos pelaa ja on spurgu
    if current_alcohol >= 2000:
        print("Ei edest darra pukki kestää näin suurta määrää alkoholia\n"
                  "Olet saanut alkoholi myrkytyksen ja kuollut vitun spurgu\n")
        hävijö = True
        continue

    # kattoo jos kentässä on jotain
    goal = Kentan_tehtava(peli_id, current_icao)
    if goal:
        print(f"\nSaavutua kentälle löysit:  {goal['name']}")
        print(f" {goal['money']}ml alkoholia")
        vastaus = input("Haluatko sen? Kyllä/ei: ").upper()

        if vastaus == "KYLLÄ":
            # Lisää tehtävän listaan ja päivitää merkit ja alkoholin määrän
            current_alcohol += goal['money']
            currentgoal += 1

            cursor = Yhdiste.cursor(dictionary=True)
            sql = "UPDATE game SET alcohol = %s WHERE id = %s"
            cursor.execute(sql, (current_alcohol, peli_id))

            print("=" * 30)
            print(f"Otit merkin : {currentgoal}/{numofgoals}")
            print(f"Sinulla on nyt {current_alcohol}ml alkoholia")
            print("=" * 30)

            # Kysyy pelaajalta haluaako pelata minipelia
            minigame_choice = input("Valitse minipeli: 1 Noppa, 2 Blackjack: taikka entter jos et halua pelata")
            print("=" * 30)
            if minigame_choice == "1":
                voitit = miniPelit.Noppa.play_noppa()
                if voitit:
                    currentgoal += 1
                    print("Voitit minipelin! Sait lisämerkin.")
                    print("=" * 30)

            elif minigame_choice == "2":
                voitit = miniPelit.BlackJack.play_blackjack()
                if voitit:
                    currentgoal += 1
                    print("Voitit minipelin! Sait lisämerkin.")
                    print("=" * 30)

            else:
                print("Virheellinen valinta, ei pelata minipeliä.")

            if currentgoal >= numofgoals:
                voitto = True
                hävijö = False
                print("=" * 30)
                print(f"Sinulla on {currentgoal} merkkiä!")
                print("=" * 30)
                break


# oiva 6/3/2026 Huomasin hauskan jutun äsken alkoholin juominen pystyy pelastamaan pelaajan alkoholi myrkytyksesta
# Oiva KRISTIAN 8/3/2026 HYYS HYYS SE ON KIVA PELI JUTTU TURPAKII ET SIE OSAA PASKAAKAA TEHÄ
# BANAANI 9/3/2026 IT JUST WORKS
#Banaani 15/4 EN KORJANNU PASKAAKAA MUT SE ON NYT EVEN WEIRDER WOOOO

# kysyy pelaajalta jos tämä tahtoo pidentaa matkustus pituutaan uhraamalla vähän alkoholia
    print("=" * 30)
    Valmis = input("Ennen kuin aloitat halutko lisätä matkustus pituuttasi 500m juomalla 200ml alkohlolia?\n"
                   "Kyllä/ei\n ").upper()
    # jos pelaja kirjoitti KYLLÄ
    if Valmis== "KYLLÄ":
        if current_alcohol >= 200:
            new_range = current_range + 500
            new_alcohol = current_alcohol - 200

            cursor = Yhdiste.cursor(dictionary=True)
            sql = "UPDATE game SET alcohol = %s WHERE id = %s"
            cursor.execute(sql, (new_alcohol, peli_id))

            # Päivitää alkoholin ja liikumis määrän uusiksi jos pelaaja juo alkoholia
            current_range = new_range
            current_alcohol = new_alcohol
            print("=" * 30)
            print(f"\nPäätit juoda osan pukin alkohlista pukki on nyt saanut enemmän taikavoimia ja pystyy lentämään pidemälle")
            print(f"Uusi liikumis pituutesi on : {new_range}m")
            print(f"Pukki joi 200ml alkoholi varoistasi uusi alkoholi määräsi on nyt  {new_alcohol}ml\n")

            # kysyy jos pelaaja halaa ruveta alkoholistiksi "enemmän kuin hän jo on"
            print("=" * 30)
            LisäC2H5OH=input("Haluato saada vielä enemmän liikumis matkaa voit juoda toiset 200ml alkoholia ja saada lisä 500m matkaa\n"
                             ":Kyllä/ei").upper()
            if LisäC2H5OH == "KYLLÄ":
                if current_alcohol >= 200:  # päivitetty alkhoholin määrä

                    # 1/5 mahdollisuus että pelaaja juo liikaa ja saa alkoholi myrkytyksen
                    if random.randint(1, 5) == 1:
                        print("=" * 30)
                        print("Pukin maksa ei kestänyt alkoholia ja pukki on kuollut alkoholi myrkytyksestä\n"
                              "HÄVISIT PELIN\n"
                              f"Sait kerättyä vain {currentgoal}/{numofgoals}merkki")
                        hävijö = True
                        break

                    else:
                        new_range = current_range + 500
                        new_alcohol = current_alcohol - 200

                        cursor = Yhdiste.cursor(dictionary=True)
                        sql = "UPDATE game SET alcohol = %s WHERE id = %s"
                        cursor.execute(sql, (new_alcohol, peli_id))

                        # Päivitää alkoholin ja liikumis määrän uusiksi jos pelaaja juo alkohlia uudestaan
                        current_range = new_range
                        current_alcohol = new_alcohol

                        # printaa nämä jos pelaajalla riitää alkohlit
                        print("=" * 30)
                        print(" päätit juoda enemmän alkoholia sait vielä toiset 500m matkaa")
                        print(f"Uusi liikumis matkasi on {new_range}m")
                        print(f"olet nyt juonut 400ml alkoholia vvähäisistä varoistasi sinulla on nyt vain  {new_alcohol}ml alkoholia :(\n")

                    #printaa tämän jos ei riitä
                else:
                    print("=" * 30)
                    print(f"Alkoholi määräsi eivät riitä tähän sinulla on vain :  {new_alcohol}ml alkohlia tarvitset minimi 200ml\n")

    # Kysytään pelaajalta minne lentää seuraavaksi
    print("=" * 30)
    print(f"{current_alcohol}")
    print("Valitse seuraava lentokenttä:")
    for i, kentta in enumerate(kaikki_kentat, 1):
        print(f"{i}. {kentta['name']} ({kentta['ident']})")

    print("=" * 30)

    try:
        valinta = int(input("Valintasi (numero): ")) - 1
        if 0 <= valinta < len(kaikki_kentat):
            uusi_kentta = kaikki_kentat[valinta]['ident']

            # Jos pelaaja kirjoitaa nykyisen sijaintinsa tämän määränpääksi printaa tämän ja kysyy uudestaan
            if uusi_kentta == current_icao:
                print("Et voi lentää kentälle jossa jo olet")
                continue

            # Lasketaan etäisyys kahden kentän välillä
            old_info = get_airport_info(current_icao)
            new_info = get_airport_info(uusi_kentta)

            lat1, lon1 = old_info[0]['latitude_deg'], old_info[0]['longitude_deg']
            lat2, lon2 = new_info[0]['latitude_deg'], new_info[0]['longitude_deg']

            # Etäisyys metreinä
            distance = int(((lat2-lat1)**2 + (lon2-lon1)**2)**0.5 * 300)

            # Tarkistaa jos pelaajan liikumis pituus on tarpeeksi
            if distance > current_range:
                print(f"Valitsemasi lentokenttä on liian kaukana. Matka kentälle on : {distance}m, maksimi pituus jota vpoit matkustaa on: {current_range}m")
                continue

            # Kun pelaaja liikkuu kenttien välillä vähenetään alkoholin määrää
            alcohol_used = max(200, int(distance / 10))
            new_alcohol = current_alcohol - alcohol_used

            cursor = Yhdiste.cursor(dictionary=True)
            sql = "UPDATE game SET location = %s, alcohol = %s WHERE id = %s"
            cursor.execute(sql, (uusi_kentta, new_alcohol, peli_id))

            print(f"\nLensit {distance}m ja käytit {alcohol_used}ml alkoholia")
            print(f"Sinulla on nyt {new_alcohol}ml alkoholia\n")
        else:
            print("Kirjoitamasi numero/luku ei ole listalla yritälkää uudestaan.")

    # printää tän jos pelaaja kirjoittaa jotain joka ei ole listassa
    except ValueError:
        print("Ooko nää juonu ku ei ossaa luke numeroita listasta")
