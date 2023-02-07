jP=10
gP=19
jK=[1,2,3,4,5]
jG=[1,2,3,4,]

def jatekos_nyer():
    if jP>gP and jP==21:
        print("Játékos nyert 21 ponttal")
    elif jP>gP and len(jK)>len(jG) and jP == 19:
        print("19 ponttal, de több lappal mint a gép")
    elif jP > gP and len(jK) < len(jG) and jP == 19:
        print("19 ponttal, de kevesebb lappal mint a gép")

def gep_nyer():
    if jP<gP and gP==21:
        print("Gép nyert 21 ponttal")
    elif jP<gP and len(jK)<len(jG) and gP == 19:
        print("19 ponttal, de több lappal mint a Játékos")
    elif jP < gP and len(jK) > len(jG) and gP == 19:
        print("19 ponttal, de kevesebb lappal mint a Játékos")

gep_nyer()
jatekos_nyer()
