# kirjoita miten alkoholi on polttoiane ja sen miten pelin häviää jos vaikka alkoholi loppuu.
# kirjoita myös mitä tapahtuu kun voitat eli keräät kaikki haalarimerkit.
# 10 haalarimerkkiä ja kun voittaa saa erikois haalarimerkin
from os.path import join

# Alkoholi polttoaine ja miten häviää
import mysql.connector
import random
yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='1507:Chris!05',
         autocommit=True
         )

# -- ohjelma alkaa tästä --

def polttoaine_positiivinen():
    print("Vrummm vrummm vrummm")
    # pelaaja liikkuu jotenkin perkele
    return polttoaine_positiivinen

def polttoaine_negatiivinen():
    #sql = "SELECT alcohol FROM game"


    print("Hävisit pelin koska olet niin vitun paska juomaan!!! ")
    # pelaaja vittu häviää koska se on paska
    return polttoaine_negatiivinen


def polttoaine_liikaa():
    print("Hävisit pelin koska olet vitun juoppo!!! ")
    # pelaaja taas vittu häivää koska se on vitun juoppo
    return polttoaine_liikaa

def voitto():
    print("Jeee voitit sait kaikki haalarimerkit tässä on erikois apro merkki")
    # Kun pelaaja kerää kaikki haalarimerkit se voittaa ja tähän tulee koodi voitto ruudulle
    return voitto


def lista_lukumaara():
    perkele = len(haalarimerkit_lista)
    if perkele == 10:
        voitto()
    return lista_lukumaara



# -- Pääohjelma --

# alkoholin väliaikainen määrrittely
# alkoholi = int(input("Montako alkoholi juomaa juot? (1-10) jos ylität 10 häviät pelin "))
haalarimerkki = input("Keräätkö haalarimerkin? (joo tai ei) ")
alkoholi = random.randint(0,10)
haalarimerkit_lista = []



while alkoholi > 0:
    polttoaine_positiivinen()
    if haalarimerkki == "joo":
        haalarimerkit_lista.append(haalarimerkki)
        print("Sinulla on haalarimerkkejä tällä hetkellä",len(haalarimerkit_lista))
        lista_lukumaara()
    elif haalarimerkki == "ei":
        print("EI oo mahdollista vittu perkele vittu vittu DUADUSHADOIDHWAOIDJAOW")

    alkoholi = random.randint(0,10)
    print(f"Joit {alkoholi} juomaa! ")
    if alkoholi < 1:
        polttoaine_negatiivinen()
    if alkoholi > 10:
        polttoaine_liikaa()



#int(input("Montako alkoholi juomaa juot? (1-10) jos ylität 10 häviät pelin "))
    #if alkoholi < 1:
        #polttoaine_negatiivinen()
    #if alkoholi > 10:
        #polttoaine_liikaa()
    #haalarimerkki = input("Keräätkö haalarimerkin? (joo tai ei) ")