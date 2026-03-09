# Kirjoitan funktio tai koodin, joka laskee etäisyyden appropiste1
#ja appropiste 2 väliltä, esim. piste 1k - piste 2k = väli/matka on 1k


import random

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

haalarimerkki = int(input("Kuinka monta haalarimerkki on?:"))

if haalarimerkki >= 10:
    print("Sinulla on 10/10 haalarimerkkiä, tässä sulle uusi erikoihaalarimerkki!")
else:
    print("Me hakee lisää haalarimerkkiä!")




# Kuinka paljon alkoholi kuluu per metri, Alkoholi 1 Litra per Kilometri

kulutus = 1000

#Funktio laskee alkoholin kulutuksen
def kulutus(matka):
    litrat = matka/ 1000
    return litrat

tulos = kulutus(matka)


print("Alkoholia kuluu", tulos,"litraa")



