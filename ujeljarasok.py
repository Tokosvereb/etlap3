
def italok():
    italkerdes:str=input("Szeretne kérni italt? (I/N) :")
    italara = 0
    for i in range(len(itallista)):
        ital_ar[itallista[i]] = ital_ar[i]
    if italkerdes == 'I' or italkerdes == 'i':
        milyetakar:str=input("Kérem válasszon a fenti listából!")
        if milyetakar == "cola" or "sprite":
            print("Hozzáadva!")
        else:
            print("Helytelen teméket adtál meg, kérlek add meg újra!")
        if italkerdes == 'N' or italkerdes == 'n':
            levesek()
    return italara

def levesek():
    leveskerdes:str=input("Szeretne kérni levest? (I/N) :")
    leveslista ={}
    levesara = 0
    for i in range(len(leveslista)):
        ital_ar[leveslista[i]] = ital_ar[i]
    if leveskerdes == 'I' or leveskerdes == 'i':
        milyetakar:str=input("Kérem válasszon a fenti listából!")
        if milyetakar == "sajtleves" or "husleves":
            print("Hozzáadva!")
        else:
            print("Helytelen teméket adtál meg, kérlek add meg újra!")
        if leveskerdes == 'N' or leveskerdes == 'n':
            foetelek()
    return levesara

def foetelek():
