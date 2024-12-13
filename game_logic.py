import random
from collections import Counter

class RockPaperScissors:
    """Class to handle Rock, Paper, Scissors game logic."""

    VALID_CHOICES = ['rock', 'paper', 'scissors']

    def __init__(self):
        self.player_history = []
        self.last_player_move = None

    def validate_choice(self, choice: str) -> bool:
        """Validate if the player's choice is valid."""
        return choice in self.VALID_CHOICES

    def random_choice(self) -> str:
        """Algorithm 1: Random choice."""
        return random.choice(self.VALID_CHOICES)

    def pattern_based_choice(self) -> str:
        """Algorithm 2: Chose based on the player's most frequent past choices."""
        if not self.player_history:
            return self.random_choice()
        most_common = Counter(self.player_history).most_common(1)[0][0]
        return self.counter_move(most_common)

    def counter_predictive_choice(self) -> str:
        """Algorithm 3: Predict and counter the player's last move."""
        if not self.last_player_move:
            return self.random_choice()
        return self.counter_move(self.last_player_move)

    def counter_move(self, move: str) -> str:
        """Return the move that beats the given move."""
        counter_moves = {'rock': 'paper', 'paper': 'scissors', 'scissors': 'rock'}
        return counter_moves[move]

    def decide_winner(self, player_move: str, computer_move: str) -> str:
        """Decide the winner of the round."""
        if player_move == computer_move:
            return 'Draw'
        if (player_move == 'rock' and computer_move == 'scissors') or \
           (player_move == 'paper' and computer_move == 'rock') or \
           (player_move == 'scissors' and computer_move == 'paper'):
            return 'Player'
        return 'Computer'
