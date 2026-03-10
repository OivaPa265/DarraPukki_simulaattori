import random
import sys


# ------------------ Rehmanin osuus ohjelmasta alkaa tästä ---------------------


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



# ----------------- Christopherin osuus ohjelmasta alkaa tästä ---------------------

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


# -- Pääohjelma --

# alkoholin väliaikainen määrrittely
# alkoholi = int(input("Montako alkoholi juomaa juot? (1-10) jos ylität 10 häviät pelin "))

alkoholi = random.randint(0,10)
haalarimerkit_lista = []



while alkoholi > 0:
    print("=========================================")
    haalarimerkki = input("Keräätkö haalarimerkin? (paina Enter) ")
    print("- - - - - - - - - - - - - - - - - - - - -")
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
    print("=========================================")
    juo = input("Kaadanko kurkustasi bisseä? (paina Enter)")
    print("- - - - - - - - - - - - - - - - - - - - -")
    if juo == "":
        alkoholi = random.randint(0,26)
        print("- - - - - - - - - - - - - - - - - - - - -")
        print(f"Kaadoin kurkustasi alas {alkoholi} juomaa! ")
        pelaajan_liike()