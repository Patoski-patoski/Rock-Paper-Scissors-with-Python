
myList = ['R', 'P', 'S']

Rock = 'R'
Paper = 'P' 
Scissors = 'S'

def chess():
    print("Rock:", Rock)
    print("Paper:", Paper)
    print('Scissors:', Scissors)
    print()
    pick = input("Player, pick your move: ")
    while pick not in myList:
        print("Invalid input")
        print()
        print("Rock:", Rock)
        print("Paper:", Paper)
        print('Scissors:', Scissors)
        
        
        pick = input("Pick your move: ")
    if pick == Rock:
        picked = "Rock"
        print("Player chose (Rock)")
    elif pick == Paper:
        picked = "Paper"
        print("Player chose (Paper)")
    elif pick == Scissors:
        picked = "Scissors"
        print("Player chose (Scissors)")
    import random
    CPU = random.choice(myList)
    print()
    print("Rock:", Rock)
    print("Paper:", Paper)
    print('Scissors:', Scissors)
    if CPU == Rock:
        CPU_picked = "Rock"
        print()
        print("CPU chose (Rock)")
    elif CPU == Paper:
        print()
        print("CPU chose (Paper)")
        CPU_picked = "Paper"
    elif CPU == Scissors:
        print()
        print("CPU chose (Scissors)")
        CPU_picked = "Scissors"
    print()
    print(f"Player ({picked}) : CPU ({CPU_picked})")
    print()

    if CPU == Rock and pick == Rock or CPU == Paper and pick == Paper or CPU == Scissors and pick == Scissors:
        print()
        print("It's a Tie")
        print()
        return chess()
        
    
    
        
    if winner(picked, CPU_picked):

        return "Player won"
    return "CPU won"

def winner(picked, CPU_picked):
    if (picked == "Rock" and CPU_picked == "Scissors") or (picked == "Paper" and CPU_picked == "Rock") or (picked == "Scissors" and CPU_picked == "Paper"):
        return True

print(chess())