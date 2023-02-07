


def eredmeny():
    jP = 22
    gP = 22
    jK = [1, 2, 3, 4, 5]
    jG = [1, 2, 3, 4]
    def jatekos_nyer():
        if jP > gP and jP == 21:
            print("Játékos nyert 21 ponttal")
        elif jP > gP and len(jK) > len(jG) and jP == 19:
            print("19 ponttal, de több lappal mint a gép")
        elif jP > gP and len(jK) < len(jG) and jP == 19:
            print("19 ponttal, de kevesebb lappal mint a gép")
        else:
            print("Játékos nyer: semmi")

    def gep_nyer():
        if jP < gP and gP == 21:
            print("Gép nyert 21 ponttal")
        elif jP < gP and len(jK) < len(jG) and gP == 19:
            print("19 ponttal, de több lappal mint a Játékos")
        elif jP < gP and len(jK) > len(jG) and gP == 19:
            print("19 ponttal, de kevesebb lappal mint a Játékos")
        else:
            print("Gép nyer: semmi")

    def dontetlen():
        if jP == gP and jP == 21 and gP == 21:
            print("Egyformán 21 pontjuk van")
        elif jP == gP and jP < 21 and gP < 21:
            print("kevesebb, mint 21, de egyforma a lapok mennyisége")
        elif jP == gP and jP > 21 and gP > 21:
            print("mindkettő meghaladta a 21, tehát minimum 22 pontjuk van")
        else:
            print("Döntetlen: semmi")

    jatekos_nyer()
    gep_nyer()
    dontetlen()
eredmeny()

