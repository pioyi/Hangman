class Hangman():
    def __init__(self, word, attempts = 6):
        self.word = word.lower()
        self.lives = attempts
        self.guesses = [' ']
    
    def get_input(self):
        char = input("Insert a character: ").lower()
        return char if char not in self.guesses else self.get_input()

    def player_turn(self):
        char = self.get_input()
        self.guesses.append(char)

        if char not in self.word:
            self.lives -= 1

    def has_winner(self):
        return all(x in self.guesses for x in self.word)

    def render_word(self):
        print(' '.join(x if x in self.guesses else "-" for x in self.word))

    def start_game(self):
        while self.lives > 0 and not self.has_winner():
            print(f"\n❤  Lives Left: {self.lives}\n")

            self.render_word()
            print(f"Attempted Characters: {sorted(self.guesses[1:])}")
            self.player_turn()

        if self.has_winner():
            print("\nCongratulations, you won!")
        else:
            print("\nI'm sorry but you have lost...")
    
game = Hangman("Python Hangman")

# Custom lives, Default = 6
# game2 = Hangman("Word",12)

game.start_game()