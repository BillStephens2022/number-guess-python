import random
from art import logo

print(logo)
print("Welcome to the Number Guess game!")
print("I'm thinking of a number between 1 and 100.")

def prompt_user_difficulty():
    invalid_answer = True
    number_of_guesses = 0
    while invalid_answer:
        difficulty = input("Choose a difficulty.  Type 'easy' or 'hard': ")
        difficulty_guesses = {"easy": 10, "hard": 5}
        if difficulty == "easy":
            number_of_guesses = difficulty_guesses[difficulty]
            invalid_answer = False
            return number_of_guesses
        elif difficulty == "hard":
            number_of_guesses = difficulty_guesses[difficulty]       
            invalid_answer = False
            return number_of_guesses
        else:
            print(f"invalid entry, please type 'easy' or 'hard'")

def pick_number():
    random_number = random.randint(1, 100)
    return random_number

number_of_guesses = prompt_user_difficulty()
print(f"you have {number_of_guesses} attempts remaining to the guess the number.")
selected_number = pick_number()
print(selected_number)