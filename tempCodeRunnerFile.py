import random

number = random.randint(1,100)

guess = int(input("pick a number from 1 to 100:"))

attempts = 0

while guess != number:
     if guess > number:
        print("TOO HIGH!")

     elif guess < number:
        print("TOO LOW!")

     attempts = attempts + 1    

     guess = int(input("try again!:"))

print("CONGRATULATIONS!!! YOU WONN!")
print("ATTEMPTS:",attempts)