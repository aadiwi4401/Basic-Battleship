print(" ")
print(" ")
print(" ---         __     ----------- -----------  |          -------                ----     |       |  -----------   ------   ")
print("|    \     /    \        |           |       |         |                     /      \   |       |       |       |       \ ")
print("|     |   /      \       |           |       |         |                    |           |       |       |       |        |")
print("|    /   |        |      |           |       |         |                     \          |       |       |       |       / ")
print("| <      |--------|      |           |       |         |-------                ----     |-------|       |       |------   ")
print("|    \   |        |      |           |       |         |                            \   |       |       |       |         ")
print("|     |  |        |      |           |       |         |                             |  |       |       |       |         ")
print("|    /   |        |      |           |       |         |                     \      /   |       |       |       |         ")
print(" ---     |        |      |           |        --------  -------                ----     |       |  -----------  |         ")
print(" ")
print(" ")
print("Player 1's Ships")
print("________________")
Ship_1 = input("Where will you place ship 1? (Capital Letter(A-J)#1-9) ")
Ship_2 = input("Where will you place ship 2? (Capital Letter(A-J)#1-9) ")
Ship_3 = input("Where will you place ship 3? (Capital Letter(A-J)#1-9) ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print("Player 2's Ships")
print("________________")
Ship_4 = input("Where will you place ship 4? (Capital Letter(A-J)#1-9) ")
Ship_5 = input("Where will you place ship 5? (Capital Letter(A-J)#1-9) ")
Ship_6 = input("Where will you place ship 6? (Capital Letter(A-J)#1-9) ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
while True:
    print(" ")
    print(" ")
    print("Player 1's Turn:")
    print("________________")
    while True:
        sum_1 = str(Ship_4) + str(Ship_5) + str(Ship_6)
        if sum_1 == '111':
            break
        strike = input("Where will you strike? (Capital letter#)")
        if strike == Ship_4:
            print("Hit!")
            print("Ship 4 has been destroyed!")
            Ship_4 = 1
            if strike == Ship_4:
                break
        elif strike == Ship_5:
            print("Hit!")
            print("Ship 5 has been destroyed!")
            Ship_5 = 1
            if strike == Ship_5:
                break
        elif strike == Ship_6:
            print("Hit!")
            print("Ship 6 has been destroyed!")
            Ship_6 = 1
            if strike == Ship_6:
                break
        else:
            print("miss")
            if strike != 0:
                break
    sum_1 = str(Ship_4) + str(Ship_5) + str(Ship_6)
    if sum_1 == '111':
        break
    print(" ")
    print(" ")
    print("Player 2's Turn:")
    print("________________")
    while True:
        sum_2 = str(Ship_1) + str(Ship_2) + str(Ship_3)
        if sum_2 == '111':
            break
        strike = input("Where will you strike? (Capital letter#)")
        if sum_1 == '111':
            break
        if strike == Ship_1:
            print("Hit!")
            print("Ship 1 has been destroyed!")
            Ship_1 = 1
            if strike == Ship_1:
                break
        elif strike == Ship_2:
            print("Hit!")
            print("Ship 2 has been destroyed!")
            Ship_2 = 1
            if strike == Ship_2:
                break
        elif strike == Ship_3:
            print("Hit!")
            print("Ship 3 has been destroyed!")
            Ship_3 = 1
            if strike == Ship_3:
                break
        else:
            print("miss")
            if strike != 0:
                break
    sum_2 = str(Ship_1) + str(Ship_2) + str(Ship_3)
    if sum_2 == '111':
        break
print(" ")
print("_________")
print(" ")
print("_________")
print(" ")
if sum_1 == '111':
    print("Player 1 Wins!")
elif sum_2 == '111':
    print ("Player 2 Wins!")