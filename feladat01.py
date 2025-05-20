import math
#1. feladat
gyujtes = str(input("Kérem adja meg, hogy mire gyűjt Anna pénzt: "))
#2. feladat
kutyak = int(input("Kérem adja meg, hogy hány kutyát sétáltat Anna a hétvégén: "))
#3. feladat
egykutya = 20   #minden kutyára 20 percet szán
kutyasetaltatas = 20 * kutyak
kutyasetaltatas_ora = math.floor(kutyasetaltatas / 60)
kutyasetaltatas_perc = kutyasetaltatas % 60
print(f"Anna összesen {kutyasetaltatas_ora}:{kutyasetaltatas_perc} percet tölt kutyasétáltatással")
#4. feladat
#egy kutyáért 700ft
kutya = 700
#5. feladat
fizetes = kutyak * kutya
print(f"Összesen {fizetes} Ft-ot keres Anna")
#6. feladat
#legalább 5000 forint a gyűjtés
if fizetes >= 5000:
    print(f"Anna {kutyak} kutyát sétáltatott {kutyasetaltatas_ora} óra {kutyasetaltatas_perc} perc alatt, ezért {fizetes} Ft-ot kapott, ez már elég a(z) {gyujtes}ra")
else:
    print(f"Anna {kutyak} kutyát sétáltatott {kutyasetaltatas_ora} óra {kutyasetaltatas_perc} perc alatt, ezért {fizetes} Ft-ot kapott, ez még nem elég a(z) {gyujtes}ra")
