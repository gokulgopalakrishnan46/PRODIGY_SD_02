import random
import tkinter as tk
from tkinter import messagebox

class GameWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Number Guessing Game")
        self.geometry("300x150")

        self.secret_number = random.randint(1, 100)
        self.total_guesses = 0

        self.label = tk.Label(self, text="Enter a number between 1 and 100:")
        self.label.pack(pady=10)

        self.entry = tk.Entry(self)
        self.entry.pack(pady=10)

        self.button = tk.Button(self, text="Submit", command=self.submit_guess)
        self.button.pack(pady=10)

    def submit_guess(self):
        guess = int(self.entry.get())

        if guess < 1 or guess > 100:
            messagebox.showerror("Error", "Your guess must be between 1 and 100. Please guess again.")
        else:
            self.total_guesses += 1

            if guess == self.secret_number:
                messagebox.showinfo("Congratulations", f"You guessed the secret number in {self.total_guesses} guesses!")
                self.destroy()
            elif guess < self.secret_number:
                messagebox.showinfo("Incorrect", "Your guess was too low. Try again.")
            else:
                messagebox.showinfo("Incorrect", "Your guess was too high. Try again.")

if __name__ == "__main__":
    app = GameWindow()
    app.mainloop()