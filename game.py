import random
import os

player_score = 0
com_score = 0

suit_obj = ["", "Gunting", "Batu", "kertas"]
player_pick = None
while player_pick != 0:
    os.system ("cls")
    print(f"player [{player_score}]:[{com_score}] komputer")
    for i in range(1, 4):
     print (f"{i}, {suit_obj[i]}")
    print()
    print("0. keluar")
    player_pick = int(input())
    if player_pick != 0:
        print(f"pilihan?? {suit_obj[player_pick]}")

        com_pick = random.randint(1,3)
        print(f"pilihan lawan{suit_obj[com_pick]}")

        if player_pick == com_pick:
            print("seri")
        else:
            if (player_pick == 1 and com_pick == 2) or (player_pick == 2 and com_pick == 3) or (player_pick == 3 and com_pick == 1):
                print("win")
                player_score +=1
            else:
                print(" lose, try again")
                com_score +=1

input ("enter to continue") 