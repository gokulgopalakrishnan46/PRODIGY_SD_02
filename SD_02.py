import random

def guess_the_number():
    secret_number = random.randint(1, 100)
    
    attempts = 0
    guessed = False

    print("Welcome to the Guess the Number game!")

    while not guessed:
        guess = int(input("Enter your guess (between 1 and 100): "))
        
        attempts += 1

        if guess == secret_number:
            guessed = True
            print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
        elif guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

if __name__ == "__main__":
    guess_the_number()