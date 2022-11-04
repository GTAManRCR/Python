"""Megkérdezzük a felhasználót, akarja-e futtatni. Ha igen, akkor nekünk kell fantázia. Írni kell egy olyan szöveges környezetet, amiben történetet mesélünk el, és amiben a felhasználó
minimum tízszer választhat lehetőségek közül. Választásoknak megfelelően lesznek különböző történetszálak, nekünk számolnunk kell, és meg kell jegyeznünk a jó döntést, és a tíz választásból
kapunk egy százalékot, ami alapján kiértékeljük a helyes válaszokat"""

futtatas=input("Akarja futtatni a programot? ")
while futtatas=="":
    futtatas=input("Akarja futtatni a programot? ")
while "igen" in futtatas or "Igen" in futtatas or "IGEN" in futtatas:
    try:
        nev=input("Kérem adja meg a nevét: ")
        print("Üdvözöljük tisztelt {}! Ebben a programban egy történetet kell kiegészítenie\n".format(nev))
        print("Elmentem sétálni az erdőbe szabadidőben, de elfelejtettem vizeletet üríteni. Elkezdett csípni a vizelet, ezután...\n")
        bemenet1=int(input("Kérem folytassa a történetet!\n1. Könnyítettem magamon\n2. Bent tartottam\nVálasz: "))
        if bemenet1==1:
            print("Ön jól döntött, hogy nem a gatyájába ürített\n")
        elif bemenet1==2:
            print("Ön bevizelt, ezért büdös lett. Ezt kiszagolta a farkas, megölte, és meghalt\n")
            break
        else:
            print("HIBA: Ön rossz választ adott meg\n")
            continue
        print("Kiürítettem a vizeletet, ezután folytattam a sétát. Ezután egy töltés felé közeledtem. Ezután elkanyarodtam...\n")
        bemenet2=int(input("Kérem folytassa a történetet!\n1. Balra\n2. Jobbra\nVálasz: "))
        if bemenet2==1:
            print("Ön balra kanyarodott, ahol nekiütközött egy fának, és meghalt\n")
            break
        elif bemenet2==2:
            print("Ön jobbra kanyarodott, ahol folytatódik a töltés\n")
        else:
            print("HIBA: Ön rossz választ adott meg\n")
            continue
        print("Jobbra kanyarodás után azt vettem észre, hogy baromi hosszú a töltés. Sétáltam rajta 500 métert, majd találtam egy folyót, ami...\n")
        bemenet3=int(input("Kérem folytassa a történetet!\n1. Balra található\n2. Jobbra található\nVálasz: "))
        if bemenet3==1:
            print("Ön szerint balra található. Telitalálat!\n")
        elif bemenet3==2:
            print("Ezt nem találta el. Legurult a töltésről, és meghalt\n")
            break
        else:
            print("HIBA: Ön rossz választ adott meg\n")
            continue
        print("A folyó víze tiszta volt, és úgy éreztem, ideje egy kicsit megmártózni benne, ezért...\n")
        bemenet4=int(input("Kérem folytassa a történetet!\n1. Beleugrottam, és úsztam\n2. Kihagytam az alkalmat\nVálasz: "))
        if bemenet4==1:
            print("Ön megmártózott a folyó vízében, de az túl mély volt. Úszási tudás hiányában elsüllyedt a vízben, és meghalt\n")
            break
        elif bemenet4==2:
            print("Ön nem tud úszni, ezért jól tette, hogy kihagyta az alkalmat\n")
        else:
            print("HIBA: Ön rossz választ adott meg\n")
            continue
        print("Úszás helyett a vizet bámulva unatkoztam, ezért úgy döntöttem, hogy...\n")
        bemenet5=int(input("Kérem folytassa a történetet!\n1. Kavicsokat dobáltam bele\n2. Elhagytam a területet\nVálasz: "))
        if bemenet5==1:
            print("Kavicsokat nem szép dolog beledobálni a vízbe, ezt jegyezze meg! Ezért megfojtottuk, és meghalt\n")
            break
        elif bemenet5==2:
            print("Ön elhagyta a folyót, és folytatta a sétát\n")
        else:
            print("HIBA: Ön rossz választ adott meg\n")
            continue
        print("A töltésen tovább sétálva találkoztam egy csillámfaszlámával, ami megtámadott...\n")
        bemenet6=int(input("Kérem folytassa a történetet!\n1. Elfutottam\n2. Bevágtam neki egyet\nVálasz: "))
        if bemenet6==1:
            print("Szégyen a hasznos, de célszerű a futás. Gratulálunk, elfutott a veszély elől\n")
        elif bemenet6==2:
            print("A csillámfaszláma jelentősen erősebb volt Önnél. Az visszatámadt, és meghalt\n")
            break
        else:
            print("HIBA: Ön rossz választ adott meg\n")
            continue
        print("Az eset után ijedve szaladtam. Annyira megijedtem, hogy majdnem beszartam, végül...\n")
        bemenet7=int(input("Kérem folytassa a történetet!\n1. Kerestem egy WC-t\n2. Beszartam\nVálasz: "))
        if bemenet7==1:
            print("Ön WC-t keresett, de nem talált\n")
        elif bemenet7==2:
            print("Ez nem volt túl helyes döntés. Beürített a gatyájába, ezért egész nap büdös szagot árasztott magából, majd a szar megölte, ezért meghalt\n")
            break
        else:
            print("HIBA: Ön rossz választ adott meg\n")
            continue
        print("Nagyon csikart a belem, ezért a belemben levő nyomás csökkentése érdekében...\n")
        bemenet8=int(input("Kérem folytassa a történetet!\n1. Fingottam egyet\n2. Tovább keresgettem a toalett iránt\nVálasz: "))
        if bemenet8==1:
            print("Nagyon csikart a belem, ezért a belemben levő nyomás csökkentése érdekében fingottam egy...\n")
            bemenet9=int(input("Kérem folytassa a történetet!\n1. Kicsit\n2. Nagyot\nVálasz: "))
            if bemenet9==1:
                print("Ön egy kis fingással elérte, hogy a belében levő nyomás a felére lecsökkenjen, így nem szükséges WC-znie, de szükséges megtudni, hogy milyet\n")
                print("Nagyon csikart a belem, ezért a belemben levő nyomás csökkentése érdekében fingottam egy kis...\n")
                bemenet10=int(input("Kérem folytassa a történetet!\n1. Csendeset\n2. Hangosat\nVálasz: "))
                if bemenet10==1:
                    print("Az Ön segglehelletét senki nem hallotta\n")
                elif bemenet10==2:
                    print("Az Ön likfittyfirittye olyan hangos volt, hogy ezt a közeli kutya meghallotta, ami elindult a hang irányába, az széttépte Önt, így meghalt\n")
                    break
                else:
                    print("HIBA: Ön rossz választ adott meg\n")
                    continue
            elif bemenet9==2:
                print("Ön olyan nagyot fingott, hogy beürített a gatyájába. A szar megölte Önt, és meghalt\n")
                break
            else:
                print("HIBA: Ön rossz választ adott meg\n")
        elif bemenet8==2:
            print("Ön klotyókeresési útra indult, de nem talált klotyót továbbra sem\n")
            break
        else:
            print("HIBA: Ön rossz választ adott meg\n")
            continue
        print("Egy csínos nő közeledett felém a történtek után, és...\n")
        bemenet11=int(input("Kérem folytassa a történetet!\n1. Megerőszakoltam\n2. Kihagytam az alkalmat\nVálasz: "))
        if bemenet11==1:
            print("A nő hangosan sikoltott, ezzel megzavarta a töltés oldalában levő állatok nyugalmát, amik megtámadták Önt, így meghalt\n")
            break
        elif bemenet11==2:
            print("Önnek erősen állt a répája, de inkább kihagyta. Jól tette, ezzel elkerült egy újabb veszélyforrást\n")
        else:
            print("HIBA: Ön rossz választ adott meg\n")
            continue
        print("Egy újabb csillámfaszláma közeledett felém, ezért...\n")
        bemenet12=int(input("Kérem folytassa a történetet!\n1. Halottnak tettettem magam\n2. Hazarohantam\nVálasz: "))
        if bemenet12==1:
            print("Hiába tettette halottnak magát, a csillámfaszláma tudta, hogy csak színlel, és megölte, ezért meghalt\n")
            break
        elif bemenet12==2:
            print("Otthon édes otthon! A töltési kalandjai után megérdemli a jól megérdemelt pihenőt\nGratulálok! Ezennel végigjátszotta a játékot tisztelt {}\n".format(nev))
        else:
            print("HIBA: Ön rossz választ adott meg\n")
            continue
    except:
        print("HIBA: Ön nem számértéket adott meg\n")
        continue
    futtatas=input("Akarja futtatni a programot? ")
print("A program futása véget ért")