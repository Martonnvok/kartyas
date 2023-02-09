

def eredmeny(jatekoslapok: [int], geplapok: [int]):
    jatekospont: int = szamolas(jatekoslapok)
    geppont: int = szamolas(geplapok)
    jatekoslapok_osszeg = len(jatekoslapok)
    geplapok_osszeg = len(geplapok)
    if jatekospont <= 21 and geppont <= 21:
        if jatekospont > geppont:
            s = "Játékos nyert!"
        elif geppont > jatekospont:
            s = "Gép nyert!"
        elif geppont == jatekospont:
            if jatekoslapok_osszeg < geplapok_osszeg:
                s = "Játékos nyert!"
            elif jatekoslapok_osszeg > geplapok_osszeg:
                s = "Gép nyert!"
            else:
                s = "Döntetlen osztoztok a nyereségen"
    else:
        if jatekospont > 21:
            s = "Játékos vesztett!"
        if geppont > 21:
            s = "Gép vesztett!"
        if jatekospont > 21 and geppont > 21:
            s = "Döntetlen osztoztok a nyereségen"

    return s

def szamolas(lapok)->int:
    pontok: int = 0
    i: int = 0
    while i < len(lapok):
        pontok += lapok[i]
        i += 1
    return pontok
#tesztek
def jatekos_vesztett_teszt():
    jatekospontok = [10, 5, 7]
    geppontok = [2, 7, 9]
    #teszt
    kapott = eredmeny(jatekospontok, geppontok)
    vart = "Játékos vesztett!"
    if kapott == vart:
        print("Az első teszt sikeres!")
    else:
        print("Az első teszt megbukott")

def gep_vesztett_teszt():
    jatekospontok = [2, 7, 9]
    geppontok = [10, 5, 7]
    #teszt
    kapott = eredmeny(jatekospontok, geppontok)
    vart = "Gép vesztett!"
    if kapott == vart:
        print("A második teszt sikeres!")
    else:
        print("A második teszt megbukott")

def lapok_osszege_teszt():
    jatekospontok = [11, 11]
    geppontok = [10, 10]
    #teszt
    osszeg = szamolas(jatekospontok)
    if osszeg > 21:
        print("A harmadik teszt sikeres!")
    else:
        print("A harmadik teszt megbukott!")

def jatekos_kozelebb_teszt():
    jatekospontok = [9, 10]
    geppontok = [8, 10]
    kapott = eredmeny(jatekospontok, geppontok)
    vart = "Játékos nyert!"
    if kapott == vart:
        print("A negyedik teszt sikeres!")
    else:
        print("A negyedik teszt megbukott")

def gep_kozelebb_teszt():
    jatekospontok = [8, 10]
    geppontok = [9, 10]
    kapott = eredmeny(jatekospontok, geppontok)
    vart = "Gép nyert!"
    if kapott == vart:
        print("Az ötödik teszt sikeres!")
    else:
        print("Az ötödik teszt megbukott")

def gep_vesztett_dontetlen_teszt():
    jatekospontok = [9, 10]
    geppontok = [9, 5, 5]
    kapott = eredmeny(jatekospontok, geppontok)
    vart = "Játékos nyert!"
    if kapott == vart:
        print("A hatodik teszt sikeres!")
    else:
        print("A hatodik teszt megbukott")

def jatekos_vesztett_dontetlen_teszt():
    jatekospontok = [9, 5, 5]
    geppontok = [9, 10]
    kapott = eredmeny(jatekospontok, geppontok)
    vart = "Gép nyert!"
    if kapott == vart:
        print("A hetedik teszt sikeres!")
    else:
        print("A hetedik teszt megbukott")


def dontetlen_teszt():
    jatekospontok = [10, 10]
    geppontok = [10, 10]
    kapott = eredmeny(jatekospontok, geppontok)
    vart = "Döntetlen osztoztok a nyereségen"
    if kapott == vart:
        print("A nyolcadik teszt sikeres!")
    else:
        print("A nyolcadik teszt megbukott")

#def eredmeny2(jK: [int]):
    #jP:int=szamolas(jK)
    #gP:int=szamolas(jG)
    #jLo=len(jK)
    #gLo=len(jG)
    #jatekospont: int=szamolas(jK)
    #jLiO=len(jK)
#def eredmeny3(jG: [int]):
    #jP:int=szamolas(jK)
    #gP:int=szamolas(jG)
    #jLo=len(jK)
    #gLo=len(jG)
    #jatekospont: int=szamolas(jG)
    #gLiO=len(jG)
def jatekos_nyer_teszt():
    #osszJ=eredmeny2(jK)
    xosszG=eredmeny3(jG)
    jP = 21
    gP = 2
    jK = [1, 2, 3, 4, 5]
    jG = [1, 2, 3, 4]
    # osszJ=eredmeny2(jP, gP=0)
    # osszG=eredmeny2(gP, jP=0)
    if jP > gP and jP == 21:
        print("Játékos nyert 21 ponttal")
    elif jP > gP and len(jK) > len(jG) and jK == 19:
        print("19 ponttal, de több lappal mint a gép")
    elif jP > gP and len(jK) < len(jG) and jK == 19:
        print("19 ponttal, de kevesebb lappal mint a gép")
    else:
        print("Játékos nyer teszt: Sikeres!")


def gep_nyer_teszt():
    jP = 2
    gP = 19
    jK = [1, 2, 3, 4, 5]
    jG = [1, 2, 3, 4]
    if jP < gP and gP == 21:
            print("Gép nyert 21 ponttal")
    elif jP < gP and len(jK) < len(jG) and gP == 19:
            print("19 ponttal, de több lappal mint a Játékos")
    elif jP < gP and len(jK) > len(jG) and gP == 19:
        print("19 ponttal, de kevesebb lappal mint a Játékos")
    else:
        print("Gép nyer teszt: Sikeres!")


def dontetlen_teszt():
    jP = 22
    gP = 22
    jK = [1, 2, 3, 4, 5]
    jG = [1, 2, 3, 4]
    if jP == gP and jP == 21 and gP == 21:
        print("Egyformán 21 pontjuk van")
    elif jP == gP and jP < 21 and gP < 21:
        print("kevesebb, mint 21, de egyforma a lapok mennyisége")
    elif jP == gP and jP > 21 and gP > 21:
        print("mindkettő meghaladta a 21, tehát minimum 22 pontjuk van")
    else:
        print("Döntetlen teszt: Sikeres!")


def tesztek():
    jatekos_vesztett_teszt()
    gep_vesztett_teszt()
    lapok_osszege_teszt()
    jatekos_kozelebb_teszt()
    gep_kozelebb_teszt()
    gep_vesztett_dontetlen_teszt()
    jatekos_vesztett_dontetlen_teszt()
    dontetlen_teszt()
    jatekos_nyer_teszt()
    gep_nyer_teszt()


tesztek()






