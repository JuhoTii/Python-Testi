oikea_luku = 15
print("Arvaa luku väliltä 1-20")

while True:
    luku = int(input("Arvaa luku: "))
    if luku == oikea_luku:
        print("Arvasit oikein!")
        break
    else:
        print("Arvasit väärin, yritä uudelleen.")