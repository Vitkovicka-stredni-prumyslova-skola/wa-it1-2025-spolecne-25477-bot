soucet=skiky=0
cisla=int(input("Vaše čislo: "))
if cisla!=0:
    soucet+=cisla
    skiky+=1
while cisla!=0:
    cisla=int(input("Vaše čislo: "))
    if cisla!=0:
        soucet+=cisla
        skiky+=1
prumer=soucet/skiky
print("Součet: ", soucet, "Aritmetický průměr: ", prumer)