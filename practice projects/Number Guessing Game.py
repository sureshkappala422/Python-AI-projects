import random

print("Hi, Guess The Number./ You Have 5 Chance. Lets Gooooo....!")

low = int(input("Enter Lower Number:- "))
higher = int(input("Enter Higher Number:- "))

print(f"You Have 5  Chances to Guess the Number Bitween {low} and {higher}. Let's Start!. ")

num = random.randint(low, higher)
ch = 5
gc = 0

while gc < ch:

    gc += 1
    guess = int(input("Enter your guess: "))

    if guess == num:
        print(f'Correct! Number is {num}. You gessed it in {gc} atempts')
        break

    elif gc >= ch and guess != num:     
        print(f'Sorry your guess number is {num}. Better Luck nuxt time. ')

    elif guess > num:
        print(f'Too High, Try lower Number!')

    elif guess < num:
        print(f'Too Lower,  Try higher Number! ')