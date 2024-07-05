import re

class Player:
    def __init__(self, name):
        self.name = name
        self.secret_number = ""
        self.attempts = 0

    def set_secret_number(self):
        while True:
            number = input(f"{self.name}, set your secret number (digits only): ")
            if re.fullmatch(r'\d+', number):
                self.secret_number = number
                break
            else:
                print("Invalid input. Please enter a number consisting of digits only.")

    def make_guess(self):
        self.attempts += 1
        return input(f"{self.name}, enter your guess: ")

class MastermindGame:
    def __init__(self):
        self.player1 = Player("Player 1")
        self.player2 = Player("Player 2")

    def provide_hints(self, secret, guess):
        correct_digits = []
        for i, digit in enumerate(guess):
            if digit == secret[i]:
                correct_digits.append(digit)
            else:
                correct_digits.append("_")
        return f"Hint: {' '.join(correct_digits)}"

    def play_round(self, guesser, setter):
        while True:
            guess = guesser.make_guess()
            if guess == setter.secret_number:
                print(f"Correct! {guesser.name} guessed the number in {guesser.attempts} attempts.")
                return guesser.attempts
            else:
                hints = self.provide_hints(setter.secret_number, guess)
                print(hints)

    def play_game(self):
        self.player1.set_secret_number()
        print("\n" * 50)  
        attempts_p2 = self.play_round(self.player2, self.player1)

        self.player2.set_secret_number()
        print("\n" * 50)  
        attempts_p1 = self.play_round(self.player1, self.player2)

        if attempts_p1 < attempts_p2:
            print(f"{self.player1.name} wins with {attempts_p1} attempts! {self.player2.name} took {attempts_p2} attempts.")
        else:
            print(f"{self.player2.name} wins with {attempts_p2} attempts! {self.player1.name} took {attempts_p1} attempts.")

if __name__ == "__main__":
    game = MastermindGame()
    game.play_game()
