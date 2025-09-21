# A fun little collection of mini-programs

import random

# Number guessing game - try to find the secret number!
random_number = random.randint(1, 50)
guess_count = 0

print("Hey there! Let's play a guessing game.")
print("I'm thinking of a number between 1 and 50...")

while True:
    try:
        user_guess = int(input("Take a guess: "))
        guess_count += 1
        
        if user_guess < random_number:
            print("Too low! Try a higher number.")
        elif user_guess > random_number:
            print("Too high! Try a lower number.")
        else:
            print(f"Awesome! You got it in {guess_count} tries!")
            break
    except:
        print("Oops! Please enter a real number.")

# Grade calculator - see what letter grade you'd get
print("\nNow let's check your grade!")
while True:
    try:
        score = int(input("What was your score (0-100)? "))
        if score < 0 or score > 100:
            print("Seriously? Give me a real score between 0 and 100!")
            continue
            
        if score >= 90:
            grade = "A"
        elif score >= 80:
            grade = "B"
        elif score >= 70:
            grade = "C"
        elif score >= 60:
            grade = "D"
        else:
            grade = "F"
            
        print(f"With {score} points, you got a {grade}!")
        break
        
    except:
        print("Come on, just enter a number!")

# Movie ticket price checker
print("\nMovie time! Let's see how much your ticket costs.")
while True:
    try:
        age = int(input("How old are you? "))
        day = input("What day is it? ").lower()
        
        # Figure out base price
        if age < 13:
            price = 300
            print("Kids ticket!")
        elif age < 18:
            price = 500
            print("Teen ticket!")
        elif age < 60:
            price = 800
            print("Adult ticket!")
        else:
            price = 400
            print("Senior discount!")
        
        # Wednesday special!
        if "wed" in day or day == "3":
            print("Sweet! Wednesday discount applied!")
            price -= 100
            if price < 0:
                price = 0  # Can't have negative prices!
        
        print(f"Your ticket will cost ₹{price}")
        break
        
    except:
        print("Just enter a normal age, please!")