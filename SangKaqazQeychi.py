import random

while True :
    print("R = rock, P = paper , S = scissors")
    user = input("Please Enter a choice : ")

    rand = ["R", "P", "S"]
    computer = random.choice(rand)

    

    if user == computer:
        print("\nBoth choice is same ")
    elif user == "R":
        if computer == "S":
            print("\nUser Win")
        else:
            print("\nComputer Win")
    elif user == "P":
        if computer == "R":
            print("\nUser Win")
        else:
            print("\nComputer Win")
    elif user == "S":
        if computer == "P":
            print("\nUser Win")
        else:
            print("\nComputer Win")
      

