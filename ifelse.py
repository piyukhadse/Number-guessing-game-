# wn = 5
# wn1 = 6
# ui = int(input("Enter any number: "))
# #if u want two number consider as right then use 'OR' opertor
# if wn == ui or wn1 == ui:
#     print("u win")
# elif wn > ui:
#     print("too small")
# else:
#     print("too big")   
# INTRESTING GAME :
import random
guess_number = random.randint(1,101)
gs = str(guess_number)
# print(gs.center(3 or 4,'*'))
count = 1
number = int(input("Guess any number from 1 to 100: "))
game_over = False

while not game_over:
    if guess_number == number:
        print(f"you win in {count} guesses.....")
        game_over = True
    else:
        if guess_number > number :
           print("your guess number is too big ")
           count += 1
           print("try again...")
           number = int(input("guess again: "))
        else:
           print("your guess number is too small")
           count += 1
           print("try again...")
           number = int(input("guess again: "))


