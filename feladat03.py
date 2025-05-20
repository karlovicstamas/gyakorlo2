class Kutya:
    def __init__(self, nev, fajta, eletkor, gazdi):
        self.nev = str(nev)
        self.fajta = str(fajta)
        self.eletkor = int(eletkor)
        self.gazdi = str(gazdi)

    def __str__(self):
        return f"{self.nev} ({self.fajta}, {self.eletkor}) - gazdi: {self.gazdi} \n"

kutyakiallitas = []
#1. feladat
def beolvasas():
    with open("kutyak.txt", encoding = "utf-8") as f:
        for line in f:
            line = line.strip()
            adatok = line.split(";")
            kutya = Kutya(adatok[0], adatok[1], adatok[2], adatok[3])
            kutyakiallitas.append(kutya)
    f.close()

#2. feladat
def db():
    print(f"{len(kutyakiallitas)} kutya szerepel a listában")

#3. feladat
def fajta():
    fajta = {}
    for item in kutyakiallitas:
        if item.fajta not in fajta:
            fajta[item.fajta] = 1
    
    print(f"{len(fajta)} különböző fajta van a listában")

#4. feladat
def legidosebb():
    legidosebb = 0
    legidosebb_kutya = ""
    for item in kutyakiallitas:
        if item.eletkor > legidosebb:
            legidosebb = item.eletkor
            legidosebb_kutya = item.nev

    print(f"{legidosebb_kutya} a legidősebb kutya és {legidosebb} éves")

#5. feladat
def gazdi():
    global gazda
    gazda = str(input("Kérem adja meg egy gazdinak a nevét, akinek a kutyáit ki szeretné íratni: "))
    for item in kutyakiallitas:
        if item.gazdi == gazda:
            print(item)

#6. feladat
def ujfajl():
    with open(f"{gazda}.txt", "w", encoding = "utf-8") as ujfajl:
        for item in kutyakiallitas:
            if item.gazdi == gazda:
                kutya_neve = item.nev
                kutya_fajtaja = item.fajta
                kutya_eletkora = item.eletkor
                kutya_gazdija = item.gazdi
                ujfajl.write(f"{kutya_neve} ({kutya_fajtaja}, {kutya_eletkora}) - {kutya_gazdija} \n")
    ujfajl.close()

def main():
    beolvasas()
    db()
    fajta()
    legidosebb()
    gazdi()
    ujfajl()

main()