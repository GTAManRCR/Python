"""Kockázunk"""
import os
import random
kor=0
nyert=False
igenlista=["igen", "Igen", "IGEN", "i", "I"]
futtatas=input("Szeretne játszani? ")
while futtatas=="":
    futtatas=input("Ne nyomja le az Entert azonnal, hanem válaszoljon. Szeretne játszani? ")
while futtatas in igenlista:
    print("Üdvözli a gitárnyakú tények fajta kockajáték")
    try:
        penz=int(input("Kérem adja meg, hogy mennyi pénze van: "))
        tet=int(input("Kérem tegyen fel tétnek valamennyi pénzt. Mennyit tesz bele? "))
        korok=int(input("Kérem adja meg, hány körből álljon a játék: "))
        print("Önnél {} Ft van most és feltett tétnek {} Ft-ot".format(penz, tet))
        if tet>penz:
            print("HIBA: Önnek nincs ennyi pénze")
            continue
        while kor<korok:
            kockak=int(input("Kérem adja meg, hogy hány kockával menjen a játék: "))
            if kockak<1 or kockak>5:
                print("Nem adhat meg egynél kisebb és ötnél nagyobb értéket")
            else:
                ertek=random.randint(1, 6)*kockak
                print("A processzor által dobott kockák értéke: {}".format(ertek))
                dobas=int(input("Szeretne dobni?\n1. Igen\n2. Nem\nVálasz: "))
                if dobas==1:
                    dobott=random.randint(1, 6)*kockak
                    print("Az Ön által dobott kockák értéke: {}".format(dobott))
                    if ertek>dobott:
                        print("Sajnos ezt a kört elveszítette. Próbálja újra")
                        kor=kor+1
                        nyert=False
                        if nyert==False:
                            penz=penz-tet
                            print("Önnek {} Ft-ja van jelenleg".format(penz))
                    elif ertek==dobott:
                        print("Döntetlen. Próbálja újra")
                    else:
                        print("Gratulálok! Ön nyert!")
                        kor=kor+1
                        nyert=True
                        if nyert==True and kor!=2:
                            print("Ön megnyerte a kört. Üdvözli a következő kör")
                        if nyert==True:
                            penz=penz+tet*2
                            print("Önnek {} Ft-ja van jelenleg".format(penz))
                elif dobas==2:
                    print("Szóval nem szeretne dobni. Hát így járt. Automatikusan veszített")
                    print("Önnek {} Ft-ja van jelenleg".format(penz))
                    kor=kor+1
                else:
                    print("HIBA: Ön rossz választ adott meg")
            if kor==korok:
                kor=0
                futtatas=input("Szeretne ismét játszani? ")
                os.system("cls")
                break
            if penz==0 or penz<0:
                print("Önnek nincs pénze, ezért nem tud játszani")
                futtatas=input("Szeretne ismét játszani? ")
                os.system("cls")
                break
    except ValueError:
        print("HIBA: Ön nem számértéket adott meg")
print("A szoftver futása véget ért")