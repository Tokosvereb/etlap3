""""import etlap
etlap.jelekkelkiiras("*" , etlapmerete)
etlap.szoveg_kiiras("*", "ÉTLAP", "*",etlapmerete)
etlap.jelekkelkiiras("*" , etlapmerete)
"""

import kozos_eljarasok
kozos_eljarasok.jelekkelkiiras("*",30)
kozos_eljarasok.jelekkelkiiras("=",30)
kozos_eljarasok.jelekkelkiiras("*",30)

kozos_eljarasok.levesek("1 - Sajtkrémleves 1950 Ft","2 - Húsleves 1950 Ft")
kerdes: str =(input("Milyen levest szeretne?Kérem válasszon az 1 és 2 gombok segítségével!"))
    if leves1 == 1:
        print(leves1)
    else :
        print(leves2)


kozos_eljarasok.foetelek("1 - Bolognai Spagetti 2850 Ft","2 - Rántotthús rizzsel 3000 Ft")
kerdes: str =(input("Milyen főételt szeretne?Kérem válasszon az 1 és 2 gombok segítségével!"))

kozos_eljarasok.desszertek("1 - Tiramisu 1100 Ft","2 - Palacsinta 750 Ft")
kerdes: str =(input("Milyen desszertet szeretne?Kérem válasszon az 1 és 2 gombok segítségével!"))

kozos_eljarasok.italok("1 - Cola 750 Ft","2 - Sprite 750 Ft")
kerdes: str =(input("Milyen italt szeretne?Kérem válasszon az 1 és 2 gombok segítségével!"))


#levesek
sajtleves: str=("1 - Sajtkrémleves")
husleves: str =("2 - Húsleves")
#foetelek
spagetti: str =("1 - Bolognai Spagetti")
rantotthus: str =("2 - Rántotthús rizzsel")
#desszertek
tiramisu: str =("1 - Tiramisu")
palacsinta: str =("2 - Palacsinta")
#italok
colaital: str =("1 - Cola")
spriteital: str =("2 - Sprite")
