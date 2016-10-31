from random import randint
number = randint (0,50)
while True:
    user_number = int(input("please enter a number between 0 and 50 : "))
    if user_number < number :
        print("you're a fucking idiot it's bigger than " + str(user_number))
    elif user_number > number :
        print("you're a fucking idiot it's smaller than " + str(user_number))
    else:
        print("God finally that's the right number")
        break
