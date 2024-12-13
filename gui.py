import tkinter as tk
from tkinter import messagebox
from game_logic import RockPaperScissors
from data_manager import DataManager

class RockPaperScissorsApp:
    """Graphical User Interface for the Rock, Paper, Scissors game."""

    def __init__(self, root: tk.Tk):
        self.game = RockPaperScissors()
        self.data_manager = DataManager()
        self.root = root
        self.root.title("Rock, Paper, Scissors")

        # Title label
        self.label = tk.Label(root, text="Choose Rock, Paper, or Scissors:", font=("Arial", 14))
        self.label.pack(pady=10)

        # Player choice buttons
        self.rock_button = tk.Button(root, text="Rock", command=lambda: self.play('rock'))
        self.paper_button = tk.Button(root, text="Paper", command=lambda: self.play('paper'))
        self.scissors_button = tk.Button(root, text="Scissors", command=lambda: self.play('scissors'))

        # Pack buttons
        self.rock_button.pack(pady=5)
        self.paper_button.pack(pady=5)
        self.scissors_button.pack(pady=5)

        # Algorithm selection
        self.algorithm_label = tk.Label(root, text="Select Algorithm to Play Against:", font=("Arial", 12))
        self.algorithm_label.pack(pady=10)

        self.algorithm_choice = tk.StringVar(value="random")

        self.random_radio = tk.Radiobutton(root, text="Random", variable=self.algorithm_choice, value="random")
        self.pattern_radio = tk.Radiobutton(root, text="Pattern-Based", variable=self.algorithm_choice, value="pattern")
        self.counter_radio = tk.Radiobutton(root, text="Counter-Predictive", variable=self.algorithm_choice, value="counter")

        # Pack radio buttons
        self.random_radio.pack()
        self.pattern_radio.pack()
        self.counter_radio.pack()

        # Stats and Exit buttons
        self.stats_button = tk.Button(root, text="Show Stats", command=self.show_stats)
        self.exit_button = tk.Button(root, text="Exit", command=root.quit)

        self.stats_button.pack(pady=5)
        self.exit_button.pack(pady=5)

    def play(self, player_choice: str) -> None:
        """Play a round of Rock, Paper, Scissors based on selected algorithm."""
        algorithm = self.algorithm_choice.get()

        if algorithm == "random":
            computer_choice = self.game.random_choice()
        elif algorithm == "pattern":
            computer_choice = self.game.pattern_based_choice()
        elif algorithm == "counter":
            computer_choice = self.game.counter_predictive_choice()
        else:
            computer_choice = self.game.random_choice()  # Fallback to random

        result = self.game.decide_winner(player_choice, computer_choice)
        self.game.player_history.append(player_choice)
        self.game.last_player_move = player_choice
        self.data_manager.update_stats(result)

        messagebox.showinfo("Result", f"You chose: {player_choice}\nComputer chose: {computer_choice}\nResult: {result}")

    def show_stats(self) -> None:
        """Display the game statistics."""
        stats = self.data_manager.get_stats()
        messagebox.showinfo("Statistics", stats)

if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissorsApp(root)
    root.mainloop()
