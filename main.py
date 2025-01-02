import random                 # Importing random module 
n = random.randint(1,100)     # Initialising range of the random integer module
a = -1
guesses = 1

while (a != n):
    a = int(input("Guess the number: "))
    
    if (a > n):
        print("Enter a lower number please....")
        guesses += 1
    elif (a < n):
        print("Enter a higher number please....")
        guesses += 1

print(f"You have guessed the number '{n}' correctly, in '{guesses}' times")


print("Thank you for playing Guess the number game")