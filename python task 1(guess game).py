import random
while True:
    print("\nI'm thinking of a number between 1000 and 9999.")
    print("\nTry to guess it in 10 tries or less")
    randomNumber = random.randrange(1000,9999)
    guess= False
    chances=0
    while guess is False and chances<10:
        User_input = int(input("\nGuess any 4 digit number: "))
        if User_input < 1000 :
            print("Wrong choice!!! Choose a 4-digit number")
            continue
        elif User_input>9999 :
            print("Wrong choice!!! Choose a 4-digit number")
            continue
        chances+=1
        if User_input == randomNumber:
            guess = True
            print("R")
            print(10-chances,"numbers of tries left")
        elif User_input == randomNumber:
            guess = True
            choice_str = str(User_input)
            for i , val in enumerate(str(randomNumber)):
                if choice_str[i] != val:
                    print("A")
                    print(10-chances,"numbers of tries left")
        elif User_input != randomNumber:
            print("W")
            print(10-chances,"numbers of tries left")
        if chances == 10:
            print("You are running out of tries!!! Try again...")
    ASK_PLAYER = input("want to play again??? Then press  : ")
    if ASK_PLAYER.upper() == "Y":
        continue
    else:
        print("Thank you for playing!!")
        break




