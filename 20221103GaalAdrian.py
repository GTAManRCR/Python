"""Megkérdezzük a felhasználót, akarja-e futtatni. Ha igen, akkor nekünk kell fantázia. Írni kell egy olyan szöveges környezetet, amiben történetet mesélünk el, és amiben a felhasználó
minimum tízszer választhat lehetőségek közül. Választásoknak megfelelően lesznek különböző történetszálak, nekünk számolnunk kell, és meg kell jegyeznünk a jó döntést, és a tíz választásból
kapunk egy százalékot, ami alapján kiértékeljük a helyes válaszokat"""

futtatas=input("Akarja futtatni a programot? ")
while futtatas=="":
    futtatas=input("Akarja futtatni a programot? ")
while futtatas=="igen" or futtatas=="Igen" or futtatas=="IGEN":
    try:
        nev=input("Kérem adja meg a nevét: ")
        print("Üdvözöljük tisztelt {}".format(nev))
        print("Elmentem sétálni az erdőbe szabadidőben, de elfelejtettem vizeletet üríteni. Elkezdett csípni a vizelet, ezután...")
        bemenet1=int(input("Kérem folytassa a történetet!\n1. Könnyítettem magamon\n2. Bent tartottam\n"))
        if bemenet1==1:
            print("Ön jól döntött, hogy nem a gatyájába ürített")
        elif bemenet1==2:
            print("Ön bevizelt, ezért büdös lett. Ezt kiszagolta a farkas, megölte, és meghalt")
            break
        else:
            print("HIBA: Ön rossz választ adott meg")
            break
        print("Kiürítettem a vizeletet, ezután folytattam a sétát. Ezután egy töltés felé közeledtem. Ezután elkanyarodtam...")
        bemenet2=int(input("Kérem folytassa a történetet!\n1. Balra\n2. Jobbra\n"))
        if bemenet2==1:
            print("Ön balra kanyarodott, ahol nekiütközött egy fának, és meghalt")
            break
        elif bemenet2==2:
            print("Ön jobbra kanyarodott, ahol folytatódik a töltés")
        else:
            print("HIBA: Ön rossz választ adott meg")
            break
        print("Jobbra kanyarodás után azt vettem észre, hogy baromi hosszú a töltés. Sétáltam rajta 500 métert, majd találtam egy folyót, ami...")
        bemenet3=int(input("Kérem folytassa a történetet!\n1. Balra található\n2. Jobbra található\n"))
        if bemenet3==1:
            print("Ön szerint balra található. Telitalálat!")
        elif bemenet3==2:
            print("Ezt nem találta el. Legurult a töltésről, és meghalt")
            break
        else:
            print("HIBA: Ön rossz választ adott meg")
            break
        print("A folyó víze tiszta volt, és úgy éreztem, ideje egy kicsit megmártózni benne, ezért...")
        bemenet4=int(input("Kérem folytassa a történetet!\n1. Beleugrottam, és úsztam\n2. Kihagytam az alkalmat\n"))
        if bemenet4==1:
            print("Ön megmártózott a folyó vízében, de az túl mély volt. Úszási tudás hiányában elsüllyedt a vízben, és meghalt")
            break
        elif bemenet4==2:
            print("Ön nem tud úszni, ezért jól tette, hogy kihagyta az alkalmat")
        else:
            print("HIBA: Ön rossz választ adott meg")
            break
        print("Úszás helyett a vizet bámulva unatkoztam, ezért úgy döntöttem, hogy...")
        bemenet5=int(input("Kérem folytassa a történetet!\n1. Kavicsokat dobáltam bele\n2. Elhagytam a területet\n"))
        if bemenet5==1:
            print("Kavicsokat nem szép dolog beledobálni a vízbe, ezt jegyezze meg! Ezért megfojtottuk, és meghalt")
            break
        elif bemenet5==2:
            print("Ön elhagyta a folyót, és folytatta a sétát")
        else:
            print("HIBA: Ön rossz választ adott meg")
            break
        print("A töltésen tovább sétálva találkoztam egy csillámfaszlámával, ami megtámadott...")
        bemenet6=int(input("Kérem folytassa a történetet!\n1. Elfutottam\n2. Bevágtam neki egyet\n"))
        if bemenet6==1:
            print("Szégyen a hasznos, de célszerű a futás. Gratulálunk, elfutott a veszély elől")
        elif bemenet6==2:
            print("A csillámfaszláma jelentősen erősebb volt Önnél. Az visszatámadt, és meghalt")
            break
        else:
            print("HIBA: Ön rossz választ adott meg")
            break
        print("Az eset után ijedve szaladtam. Annyira megijedtem, hogy majdnem beszartam, végül...")
        bemenet7=int(input("Kérem folytassa a történetet!\n1. Kerestem egy WC-t\n2. Beszartam\n"))
        if bemenet7==1:
            print("Ön WC-t keresett, de nem talált")
        elif bemenet7==2:
            print("Ez nem volt túl helyes döntés. Beürített a gatyájába, ezért egész nap büdös szagot árasztott magából, majd a szar megölte, ezért meghalt")
            break
        else:
            print("HIBA: Ön rossz választ adott meg")
            break
        print("Nagyon csikart a belem, ezért a belemben levő nyomás csökkentése érdekében...")
        bemenet8=int(input("Kérem folytassa a történetet!\n1. Fingottam egyet\n2. Tovább keresgettem a toalett iránt\n"))
        if bemenet8==1:
            print("Ön a segglehelletével ott hagyott egy szagosat, de nem szart be")
        elif bemenet8==2:
            print("Ön klotyókeresési útra indult, de nem talált klotyót továbbra sem")
            break
        else:
            print("HIBA: Ön rossz választ adott meg")
            break
        print("Egy csínos nő közeledett felém a történtek után, és...")
        bemenet9=int(input("Kérem folytassa a történetet!\n1. Megerőszakoltam\n2. Kihagytam az alkalmat\n"))
        if bemenet9==1:
            print("A nő hangosan sikoltott, ezzel megzavarta a töltés oldalában levő állatok nyugalmát, amik megtámadták Önt, így meghalt")
            break
        elif bemenet9==2:
            print("Önnek erősen állt a répája, de inkább kihagyta. Jól tette, ezzel elkerült egy újabb veszélyforrást")
        else:
            print("HIBA: Ön rossz választ adott meg")
            break
        print("Egy újabb csillámfaszláma közeledett felém, ezért...")
        bemenet10=int(input("Kérem folytassa a történetet!\n1. Halottnak tettettem magam\n2. Hazarohantam\n"))
        if bemenet10==1:
            print("Hiába tettette halottnak magát, a csillámfaszláma tudta, hogy csak színlel, és megölte, ezért meghalt")
            break
        elif bemenet10==2:
            print("Otthon édes otthon! A töltési kalandjai után megérdemli a jól megérdemelt pihenőt\nGratulálok! Ezennel végigjátszotta a játékot tisztelt {}".format(nev))
        else:
            print("HIBA: Ön rossz választ adott meg")
            break
    except:
        print("HIBA: Ön nem számértéket adott meg")
        continue
    futtatas=input("Akarja futtatni a programot? ")
print("A program futása véget ért")