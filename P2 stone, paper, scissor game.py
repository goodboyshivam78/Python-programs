import random

print("----------------------------Welcome to LILY Games (STONE|PAPER|SCISSOR) ------------------------\n")
item = ['stone', 'paper', 'scissor']
name = input("Enter player name: ")
check = 'y'
while check == 'y':
    targetPoint = int(input("Enter the Target point: "))
    points = {name:0 ,"computer":0}

    while (points[name] != targetPoint and points["computer"] != targetPoint):
        user = input("Choose (stone/paper/scissor) : ")
        computer = random.choice(item)
        print(f"\n{name} = {user.capitalize()}  :  Computer = {computer.capitalize()}")
        
        if user == computer:
            print(f"{points[name]} ------TIE!------ {points['computer']}  \n")
        elif user == "stone":
            if computer == "scissor":
                points[name]+=1
                print(f"{points[name]} -----{name} +1------ {points['computer']}\n")
            else :
                points["computer"]+=1
                print(f"{points[name]} ------Computer +1------ {points['computer']}\n")
        elif user == "scissor":
            if computer == "paper":
                points[name]+=1
                print(f"{points[name]} -----{name} +1------ {points['computer']}\n")
            else :
                points["computer"]+=1
                print(f"{points[name]} ------Computer +1------ {points['computer']}\n")
        elif user == "paper":
            if computer == "stone":
                points[name]+=1
                print(f"{points[name]} -----{name} +1------ {points['computer']}\n")
            else :
                points["computer"]+=1
                print(f"{points[name]} ------Computer +1------ {points['computer']}\n")
        else :
            print("You have entered wrong item!\n")

    else :
        if points[name] == targetPoint:
            print(f"{points[name]} -----------------{name.upper()} WINS *_* ------------------- {points['computer']}")
        else :
            print(f"{points[name]} -------------------COMPUTER WINS  ^_^ --------------------- {points['computer']}")
    check = input("\nDo you want to play again #_# (y/n): ")



