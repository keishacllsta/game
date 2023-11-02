import random
import os

skor_pemain = 0
skor_komp = 0

pilihan = ["", "Gunting", "Batu", "kertas"]
pilihan_pemain = None
while pilihan_pemain != 0:
    os.system ("cls")
    print(f"player [{skor_pemain}]:[{skor_komp}] komputer")
    for i in range(1, 4):
     print (f"{i}, {pilihan[i]}")
    print()
    print("0. keluar")
    pilihan_pemain = int(input())
    if pilihan_pemain != 0:
        print(f"pilihan?? {pilihan[pilihan_pemain]}")

        pilihan_komp = random.randint(1,3)
        print(f"pilihan lawan{pilihan[pilihan_komp]}")

        if pilihan_pemain == pilihan_komp:
            print("seri")
        else:
            if (pilihan_pemain == 1 and pilihan_komp == 2) or (pilihan_pemain == 2 and pilihan_komp == 3) or (pilihan_pemain == 3 and pilihan_komp== 1):
                print("win")
                skor_pemain +=1
            else:
                print(" lose, try again")
                skor_komp +=1

input ("enter to continue") 