from random import*
print("BlackJack")
sou=0
soubota=0
kard=input("Chcete kartu?(ano,jo/ne) ")
while kard=="ano" or kard=="jo":
    carda= randint(1,11)
    cardabota= randint(1,11)
    sou+=carda
    soubota+=cardabota
    print("Vaše čislo: ",carda)
    print("Čislo počitače: ",cardabota)
    if sou==21:
        print("Vy jste vyhral/a!")
        soubota=0
        sou=0
    if sou>21:
        print("Vy jste prohral/a")
        break
    if soubota==21:
        print("Vy jste prohral/a!")
        soubota=0
        sou=0
        break
    if soubota>21:
        print("Vy jste vyhral/a. Počitač ma vic než 21!")
        soubota=0
        sou=0
        break
    elif sou<21:
        kard=input("Chcete kartu?(ano,jo/ne) ")
    


if kard=='ne':
    if soubota>sou:
        print("Vy jste prohral/a!")
    elif sou>soubota:
        print("Vy jste prohral/a!")
    else:
        print("Revize!")
    print("Vaš součet: ", sou)
    print("Součet počitače: ", soubota)
if kard!="ano" and kard!="jo" and kard!="ne":
    print("Co myslite?")
    kard=input("Chcete kartu?(ano,jo/ne) ")
