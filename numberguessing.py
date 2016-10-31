from random import randint
number = randint (0,50)
while True:
    user_number = int(input("please enter a number between 0 and 50 : "))
    if user_number < number :
        print("It's bigger than " + str(user_number))
    elif user_number > number :
        print("It's smaller than " + str(user_number))
    else:
        print("Congratiulations that's the right number")
        break
