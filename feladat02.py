kutyusok = []
def beolvasas():
    with open("kutyusok.txt", encoding = "utf-8") as f:
        for line in f:
            line = line.strip()
            kutyusok.append(line)
    f.close()

def db():
    print(f"{len(kutyusok)}db kutyanév szerepel a listában")

def ibetu():
    #i betűre végződő kutyanevek
    print('Az "i" betűre végződő kutyanevek:')
    for item in kutyusok:
        if item[-1] == "i":
            print(item)

def ismetles():
    ismetlodo_nevek = {}
    for item in kutyusok:
        if item not in ismetlodo_nevek:
            ismetlodo_nevek[item] = 0
        ismetlodo_nevek[item] += 1

    print("Az 1-nél többször előforduló kutyanevek a listában:")
    for item in ismetlodo_nevek:
        if ismetlodo_nevek[item] > 1:
            print(f"{item} - {ismetlodo_nevek[item]}")

def abc():
    while len(kutyusok) != 0:
        


def main():
    beolvasas()
    db()
    ibetu()
    ismetles()

main()