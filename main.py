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

def check_guess(guess, selected_number):
    if guess == selected_number:
        return "You win!!"
    elif guess > selected_number:
        return "Too High.\nGuess again."
    else:
        return "Too Low.\nGuess again."
        



print(logo)
print("Welcome to the Number Guess game!")
print("I'm thinking of a number between 1 and 100.")

def play_game(): 
    should_continue = True
    while should_continue:
        remaining_guesses = prompt_user_difficulty()
        print(f"you have {remaining_guesses} attempts remaining to the guess the number.")
        selected_number = pick_number()
        while remaining_guesses > 0:
            user_guess = prompt_guess()
            message = check_guess(user_guess, selected_number)
            print(message)
            if message == "You win!!":
                print("Thanks for playing!")
                should_continue = False
                remaining_guesses = 0
            else:
                remaining_guesses -= 1
                print(f"You have {remaining_guesses} attempts remaining to guess the number.")
        print("Game Over")
        should_continue = False

play_game()
play_again = input("Would you like to play again? Type 'y' or 'n': ")
if play_again == "y":
    play_game()
else:
    print("Thanks for playing, come back soon!")
            
   
    