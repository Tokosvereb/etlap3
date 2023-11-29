"""nullatol a lista hosszaig
mindig az iedik elemet kell kiirni es kapjon parametert"""
penz = 0

def rendelesMain():
    eloetelek()

def eloetelek():
   global penz
   eloetelkerdes:str=input("Szeretne kérni előételt? (I/N) :")
   if eloetelkerdes == 'I' or eloetelkerdes == 'i':
     milyetakar:str=input("Kérem válasszon a fenti listából!")
     if milyetakar == "sajtkrémleves":
       penz += 1950
       print("Hozzáadva!")
       foetelek()
     elif milyetakar == "Húsleves":
         penz += 1950
         print("Hozzáadva!")
         foetelek()
     else:
        print("Ilyen levesünk nincs!")
        eloetelek()
   elif eloetelkerdes == 'n' or eloetelkerdes == 'N':
       foetelek()
   else:
       print("HIBA: Csak I/N válasz megadása lehetséges")

def foetelek():
    global penz
    foetelkerdes:str=input("Szeretne kérni főételt?I/N")
    if foetelkerdes == 'I' or foetelkerdes == 'i':
        milyetakar2:str=input("Kérem válasszon a fenti listából!")
        if milyetakar2 == "Bolognai Spagetti":
            penz += 2850
            print("Hozzáadva!")
            desszertek()
        elif milyetakar2 == "Húsleves":
            penz += 1950
            print("Hozzáadva!")
            desszertek()
        else:
            print("Ilyen étel nincs!")
            foetelek()
    elif foetelkerdes == 'n' or foetelkerdes == 'N':
        desszertek()
    else:
        print("HIBA: Csak I/N válasz megadása lehetséges")

def desszertek():
    global penz
    desszertkerdes:str=input("Szeretne kérni desszertet?I/N")
    if desszertkerdes == 'I' or desszertkerdes == 'i':
        milyetakar3:str=input("Kérem válasszon a fenti listából!")
        if milyetakar3 == "Bolognai Spagetti":
            penz += 2850
            print("Hozzáadva!")
            uditok()
        elif milyetakar3 == "Rántotthús rizzsel":
            penz += 3000
            print("Hozzáadva!")
            uditok()
        else:
            print("Ilyen étel nincs!")
            uditok()
    elif desszertkerdes == 'n' or desszertkerdes == 'N':
        uditok()
    else:
        print("HIBA: Csak I/N válasz megadása lehetséges")

def uditok():
    global penz
    uditokerdes:str=input("Szeretne kérni üdítőt?I/N")
    if uditokerdes == 'I' or uditokerdes == 'i':
        milyetakar4:str=input("Kérem válasszon a fenti listából!")
        if milyetakar4 == "sprite":
            penz += 2850
            print("Hozzáadva!")
            vegosszeg()
        elif milyetakar4 == "Cola":
            penz += 1950
            print("Hozzáadva!")
            vegosszeg()
        else:
            print("Ilyen üdítő nincs!")
            desszertek()
    elif uditokerdes == 'n' or uditokerdes == 'N':
        vegosszeg()
    else:
        print("HIBA: Csak I/N válasz megadása lehetséges")

def vegosszeg():
    print(f"Végösszeg:{penz} Ft")