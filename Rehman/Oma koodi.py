#Löysit Baarista haalarimerkki.
#Teen koodi, ilmoitusviesti esim kun pelaaja löytää haalarimerkkin
#Niin hänelle tule ilmoitus siitä ja teen funktion joka pitää kirjaa montako haalarimerkkiä on löydetty yhteensä.


# Tässä FUnktio lisää yhden haalarimerkkin määrän
# Sen jälkeen lisää yhden haalrimerkkin ja näyttää uuden määrän
def haalarimerkki(maara):
    maara = maara + 1
    print("Haalarimerkki löydetty!")
    print("Sinulla on nyt", maara, "kpl")
    return maara

#Kysytään pelaajalta kuinka monta haalarimerkki hänellä on?
maara = int(input("Montako haalarimerkkiä sinulla on?: "))

#Kutsutaan funktiota ja päivitetään määrä.
maara = haalarimerkki(maara)





