class RockPaperScissorsGame:
    def __init__(self):
        self.choices = ['rock', 'paper', 'scissors']

    def get_choices_from_input(self, input_string):
        choices = input_string.lower().split(' vs ')
        if len(choices) != 2 or choices[0] not in self.choices or choices[1] not in self.choices:
            raise ValueError("Invalid input. Please use the format 'ROCK VS PAPER'.")
        return choices[0], choices[1]

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a draw!"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            return f"{user_choice} wins!"
        else:
            return f"{computer_choice} wins!"

    def play(self, input_string):
        try:
            user_choice, computer_choice = self.get_choices_from_input(input_string)
            print(f"You selected: {user_choice}")
            print(f"Computer selected: {computer_choice}")
            result = self.determine_winner(user_choice, computer_choice)
            print(result)
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    game = RockPaperScissorsGame()
    input_string = input("Enter choices in the format 'ROCK VS PAPER': ")
    game.play(input_string)
