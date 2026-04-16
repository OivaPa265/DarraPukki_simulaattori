def play_blackjack():
    import random

    Pukkipelissa = True
    MikkoPelissa = True

    Pakka = [2, 3, 4, 5, 6, 7, 8, 9, 10,
             2, 3, 4, 5, 6, 7, 8, 9, 10,
             2, 3, 4, 5, 6, 7, 8, 9, 10,
             2, 3, 4, 5, 6, 7, 8, 9, 10,
             "J", "Q", "K", "A", "J", "Q", "K", "A", "J", "Q", "K", "A", "J", "Q", "K", "A"]
    Kasi = []
    Mikko = []  # baarimikko

        # katsoo  kenen vuoro on
    def anna(vuoro):
        Kortti = random.choice(Pakka)
        vuoro.append(Kortti)
        Pakka.remove(Kortti)

    # korttien määrät
    def Maara(vuoro):
        summa = 0
        Kuva = ["J", "Q", "K"]
        assat = 0
        for Kortti in vuoro:
            if Kortti in Kuva:
                summa += 10
            elif Kortti == "A":
                assat += 1
            else:
                summa += Kortti

        # katsoo ässät joko 1 tai 11 riipuen kuinka paljon pelaajilla on kädessään
        for i in range(assat):
            if summa + 11 <= 21:
                summa += 11
            else:
                summa += 1
        return summa

    for i in range(2):
        anna(Mikko)
        anna(Kasi)


# katsoo jos kummatkin pelaajat pysyvät pelissä
    while Pukkipelissa or MikkoPelissa:
        print(f"\nMikolla on näkyvissä: {Mikko[0]}")
        print(f"Pukilla on: {Kasi} (Yhteensä: {Maara(Kasi)})")

        # Darra pukin vuoro
        if Pukkipelissa:
            Jatkoon = input("Otatko kortin (Y) vai lopetatko (N)? ").upper()
            if Jatkoon == "Y":
                anna(Kasi)
            elif Jatkoon == "N":
                Pukkipelissa = False
            else:
                print("Kirjoita joko Y taikka N")
                continue

        # Jos mikko pääsee 17 aloitaa "kolikko heito"
        # jos numero on 1 mikko ei ota korttia ja jos 2 ottaa kortin
        # paitsi jos yli 21
        if MikkoPelissa:
            nykyinen_mikko = Maara(Mikko)
            if nykyinen_mikko < 17:
                anna(Mikko)
            elif nykyinen_mikko < 21:
                Heitto = random.randint(1, 2)
                if Heitto == 1:
                    print(" Mikko lopetaa ")
                    MikkoPelissa = False
                else:
                    print("Mikko ottaa kortin")
                    anna(Mikko)
            else:

                MikkoPelissa = False

        if Maara(Kasi) >= 21 or (not Pukkipelissa and not MikkoPelissa):
            break

    pisteet = Maara(Kasi)
    mikon_pisteet = Maara(Mikko)

    print("" + "=" * 30)
    print(f"Pukin käsi: {Kasi} ({pisteet})")
    print(f"Mikon käsi: {Mikko} ({mikon_pisteet})")

    if pisteet > 21:
        print("Hävisit! Menit yli 21.")
        return False
    elif mikon_pisteet > 21:
        print("Voitit! Mikko meni yli 21.")
        return True
    elif pisteet > mikon_pisteet:
        print("Voitit pelin!")
        return True
    elif pisteet < mikon_pisteet:
        print("Hävisit pelin.")
        return False
    else:
        print("Tasapeli!")
        return False
