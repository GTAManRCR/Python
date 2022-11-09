"""Megkérdezzük a felhasználót, akarja-e futtatni. Ha igen, akkor nekünk kell fantázia. Írni kell egy olyan szöveges környezetet, amiben történetet mesélünk el, és amiben a felhasználó
minimum tízszer választhat lehetőségek közül. Választásoknak megfelelően lesznek különböző történetszálak, nekünk számolnunk kell, és meg kell jegyeznünk a jó döntést, és a tíz választásból
kapunk egy százalékot, ami alapján kiértékeljük a helyes válaszokat"""

igenlista=["igen", "Igen", "IGEN", "i", "I", "persze", "Persze", "PERSZE", "természetesen", "TERMÉSZETESEN", "Természetesen", "aha", "Aha", "AHA", "hogyne", "Hogyne", "HOGYNE", "Mindenképp", "mindenképp", "MINDENKÉPP", "Mindenképpen", "mindenképpen", "MINDENKÉPPEN", "mindenáron", "Mindenáron", "MINDENÁRON", "szeretném", "Szeretném", "SZERETNÉM", "akarnám", "Akarnám", "AKARNÁM", "akarom", "Akarom", "AKAROM", "miért ne?", "Miért ne?", "MIÉRT NE?", "igaz", "Igaz", "IGAZ", "ikat", "Ikat", "IKAT", "yes", "YES", "Yes", "y", "Y", "true", "True", "TRUE", "yep", "Yep", "YEP", "yup", "Yup", "YUP", "yeah", "Yeah", "YEAH", "yes i do", "Yes, I do", "YES, I DO", "i want", "I want", "I WANT", "sure", "Sure", "SURE", "why not?", "Why not?", "WHY NOT?", "of course", "Of course", "OF COURSE", "Ja", "ja", "JA", "J", "j", "Richtig", "RICHTIG", "richtig", "natürlich", "Natürlich", "NATÜRLICH", "da", "DA", "Da", "D", "d"]
futtatas=input("Akarja futtatni a programot? [Válaszolhat magyarul, angolul, németül, és oroszul is] ")
while futtatas=="":
    futtatas=input("Akarja futtatni a programot? [Válaszolhat magyarul, angolul, németül, és oroszul is] ")
while futtatas in igenlista:
    try:
        nev=input("Kérem adja meg a nevét: ")
        print("\nÜdvözöljük tisztelt {}! Ebben a programban egy történetet kell kiegészítenie\n".format(nev))
        print("Elmentem sétálni az erdőbe szabadidőben, de elfelejtettem vizeletet üríteni. Elkezdett csípni a vizelet, ezután...\n")
        bemenet1=int(input("Kérem folytassa a történetet!\n\n1. Könnyítettem magamon\n2. Bent tartottam\n\nVálasz: "))
        if bemenet1==1:
            print("\nÖn jól döntött, hogy nem a gatyájába ürített\n")
        elif bemenet1==2:
            print("\nÖn bevizelt, ezért büdös lett. Ezt kiszagolta a farkas, megölte, és meghalt\n")
            break
        else:
            print("\nHIBA: Ön rossz számértéket adott meg\n")
            continue
        print("Kiürítettem a vizeletet, ezután folytattam a sétát. Ezután egy töltés felé közeledtem. Ezután elkanyarodtam...\n")
        bemenet2=int(input("Kérem folytassa a történetet!\n\n1. Balra\n2. Jobbra\n\nVálasz: "))
        if bemenet2==1:
            print("\nÖn balra kanyarodott, ahol nekiütközött egy fának, és meghalt\n")
            break
        elif bemenet2==2:
            print("\nÖn jobbra kanyarodott, ahol folytatódik a töltés\n")
        else:
            print("\nHIBA: Ön rossz számértéket adott meg\n")
            continue
        print("Jobbra kanyarodás után azt vettem észre, hogy baromi hosszú a töltés. Sétáltam rajta 500 métert, majd találtam egy folyót, ami...\n")
        bemenet3=int(input("Kérem folytassa a történetet!\n\n1. Balra található\n2. Jobbra található\n\nVálasz: "))
        if bemenet3==1:
            print("\nÖn szerint balra található. Telitalálat!\n")
        elif bemenet3==2:
            print("\nEzt nem találta el. Legurult a töltésről, és meghalt\n")
            break
        else:
            print("\nHIBA: Ön rossz számértéket adott meg\n")
            continue
        print("A folyó víze tiszta volt, és úgy éreztem, ideje egy kicsit megmártózni benne, ezért...\n")
        bemenet4=int(input("Kérem folytassa a történetet!\n\n1. Beleugrottam, és úsztam\n2. Kihagytam az alkalmat\n\nVálasz: "))
        if bemenet4==1:
            print("\nÖn megmártózott a folyó vízében, de az túl mély volt. Úszási tudás hiányában elsüllyedt a vízben, és meghalt\n")
            break
        elif bemenet4==2:
            print("\nÖn nem tud úszni, ezért jól tette, hogy kihagyta az alkalmat\n")
        else:
            print("\nHIBA: Ön rossz számértéket adott meg\n")
            continue
        print("Úszás helyett a vizet bámulva unatkoztam, ezért úgy döntöttem, hogy...\n")
        bemenet5=int(input("Kérem folytassa a történetet!\n\n1. Kavicsokat dobáltam bele\n2. Elhagytam a területet\n\nVálasz: "))
        if bemenet5==1:
            print("\nKavicsokat nem szép dolog beledobálni a vízbe, ezt jegyezze meg! Ezért megfojtottuk, és meghalt\n")
            break
        elif bemenet5==2:
            print("\nÖn elhagyta a folyót, és folytatta a sétát\n")
        else:
            print("\nHIBA: Ön rossz számértéket adott meg\n")
            continue
        print("A töltésen tovább sétálva találkoztam egy csillámfaszlámával, ami megtámadott...\n")
        bemenet6=int(input("Kérem folytassa a történetet!\n\n1. Elfutottam\n2. Bevágtam neki egyet\n\nVálasz: "))
        if bemenet6==1:
            print("\nSzégyen a hasznos, de célszerű a futás. Gratulálunk, elfutott a veszély elől\n")
        elif bemenet6==2:
            print("\nA csillámfaszláma jelentősen erősebb volt Önnél. Az visszatámadt, és meghalt\n")
            break
        else:
            print("\nHIBA: Ön rossz számértéket adott meg\n")
            continue
        print("Az eset után ijedve szaladtam. Annyira megijedtem, hogy majdnem beszartam, végül...\n")
        bemenet7=int(input("Kérem folytassa a történetet!\n\n1. Kerestem egy WC-t\n2. Beszartam\n\nVálasz: "))
        if bemenet7==1:
            print("\nÖn WC-t keresett, de nem talált\n")
        elif bemenet7==2:
            print("\nEz nem volt túl helyes döntés. Beürített a gatyájába, ezért egész nap büdös szagot árasztott magából, majd a szar megölte, ezért meghalt\n")
            break
        else:
            print("\nHIBA: Ön rossz számértéket adott meg\n")
            continue
        print("Nagyon csikart a belem, ezért a belemben levő nyomás csökkentése érdekében...\n")
        bemenet8=int(input("Kérem folytassa a történetet!\n\n1. Fingottam egyet\n2. Tovább keresgettem a toalett iránt\n\nVálasz: "))
        if bemenet8==1:
            print("Nagyon csikart a belem, ezért a belemben levő nyomás csökkentése érdekében fingottam egy...\n")
            bemenet9=int(input("Kérem folytassa a történetet!\n\n1. Kicsit\n2. Nagyot\n\nVálasz: "))
            if bemenet9==1:
                print("\nÖn egy kis fingással elérte, hogy a belében levő nyomás a felére lecsökkenjen, így nem szükséges WC-znie, de szükséges megtudni, hogy milyet\n")
                print("Nagyon csikart a belem, ezért a belemben levő nyomás csökkentése érdekében fingottam egy kis...\n")
                bemenet10=int(input("Kérem folytassa a történetet!\n\n1. Csendeset\n2. Hangosat\n\nVálasz: "))
                if bemenet10==1:
                    print("\nAz Ön segglehelletét senki nem hallotta\n")
                elif bemenet10==2:
                    print("\nAz Ön likfittyfirittye olyan hangos volt, hogy ezt a közeli kutya meghallotta, ami elindult a hang irányába, az széttépte Önt, így meghalt\n")
                    break
                else:
                    print("\nHIBA: Ön rossz számértéket adott meg\n")
                    continue
            elif bemenet9==2:
                print("\nÖn olyan nagyot fingott, hogy beürített a gatyájába. A szar megölte Önt, és meghalt\n")
                break
            else:
                print("\nHIBA: Ön rossz számértéket adott meg\n")
        elif bemenet8==2:
            print("\nÖn klotyókeresési útra indult, de nem talált klotyót továbbra sem\n")
            break
        else:
            print("\nHIBA: Ön rossz számértéket adott meg\n")
            continue
        print("Egy csínos nő közeledett felém a történtek után, és...\n")
        bemenet11=int(input("Kérem folytassa a történetet!\n\n1. Megerőszakoltam\n2. Kihagytam az alkalmat\n\nVálasz: "))
        if bemenet11==1:
            print("\nA nő hangosan sikoltott, ezzel megzavarta a töltés oldalában levő állatok nyugalmát, amik megtámadták Önt, így meghalt\n")
            break
        elif bemenet11==2:
            print("\nÖnnek erősen állt a répája, de inkább kihagyta. Jól tette, ezzel elkerült egy újabb veszélyforrást\n")
        else:
            print("\nHIBA: Ön rossz számértéket adott meg\n")
            continue
        print("Egy újabb csillámfaszláma közeledett felém, ezért...\n")
        bemenet12=int(input("Kérem folytassa a történetet!\n\n1. Halottnak tettettem magam\n2. Hazarohantam\n\nVálasz: "))
        if bemenet12==1:
            print("\nHiába tettette halottnak magát, a csillámfaszláma tudta, hogy csak színlel, és megölte, ezért meghalt\n")
            break
        elif bemenet12==2:
            print("\nOtthon édes otthon! A töltési kalandjai után megérdemli a jól megérdemelt pihenőt\nGratulálok! Ezennel végigjátszotta a játékot tisztelt {}\n".format(nev))
        else:
            print("\nHIBA: Ön rossz számértéket adott meg\n")
            continue
    except:
        print("\nHIBA: Ön nem számértéket adott meg\n")
        continue
    futtatas=input("Akarja futtatni a programot? ")
print("A program futása véget ért")

#Ez a program 137 sorból áll, melyből a kikommentelés 3 sor, a programkód 130 sor, ezzel a megjegyzéssel együtt 137 sor összesen