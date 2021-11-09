import random
secretNum = random.randint(1,100)
guess_count=0

while True:
    answer = int(input("What is your number guess? "))
    guess_count += 1
    if answer == secretNum:
        print("Congratulations, You are correct and guessed",guess_count,"times.")
        break
    elif answer != secretNum:
        if answer > secretNum:
            print("Wrong answer, your guess is high.")
        elif answer < secretNum:
            print("Wrong answer, your guess is low.")

