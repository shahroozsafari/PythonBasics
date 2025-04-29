

import random


number = random.randrange(100,501)

for count in range(1,11) :
    print(f"Try {count} / 10 ")
    guess = int(input("Enter your number : "))
    if guess > number :
        print("Too Large ")
    elif guess < number :
        print("Too Small")
    elif guess == number :
        print("Congrats! you guess correct number.")
        break


print("==========================")

# match guess :
#     case guess if guess > number :
#         print("Too Large ")
#     case guess if guess < number :
#         print("Too Small")
#     case guess if guess == number :
#         print("Congrats! you guess correct number.")
#     case _ :
#         print("**************")
# print("==========================")