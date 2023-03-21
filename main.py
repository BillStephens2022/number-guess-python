import random
from art import logo

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

def prompt_guess():
    user_guess = int(input("Make a guess: "))
    return user_guess

def check_guess(guess, selected_number, remaining_guesses):
    if guess == selected_number:
        remaining_guesses = 0
        message = "You win"
        return message
    elif guess > selected_number:
        remaining_guesses -= 1
        message = "Too High.\nGuess again."
        return message
    else:
        remaining_guesses -= 1
        message = "Too Low.\nGuess again."
        return message

should_continue = True

print(logo)
print("Welcome to the Number Guess game!")

while should_continue:
    print("I'm thinking of a number between 1 and 100.")
    remaining_guesses = prompt_user_difficulty()
    print(f"you have {remaining_guesses} attempts remaining to the guess the number.")
    selected_number = pick_number()
    print(selected_number)
    user_guess = prompt_guess()
    message = check_guess(user_guess, selected_number, remaining_guesses)
    print(message)
    if remaining_guesses == 0:
        print(message)
        should_continue = False
    