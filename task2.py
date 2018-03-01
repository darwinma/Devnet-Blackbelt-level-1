import random

input_number = input("Guess the number from 1 to 3: ")
random_number = random.randint(1,3)

if random_number == int(input_number):
    print("Correct!")
else:
    print("Wrong! Ur guess is " + str (input_number))
    print ("The correct guess is " + str(random_number))