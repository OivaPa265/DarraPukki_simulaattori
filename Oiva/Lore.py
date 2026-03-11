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
