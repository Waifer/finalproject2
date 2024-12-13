import csv
import os

class DataManager:
    """Class to manage storing and retrieving game statistics using CSV."""

    def __init__(self, file_path: str = 'stats.csv'):
        self.file_path = file_path
        self.stats = {'wins': 0, 'losses': 0, 'draws': 0}
        self._load_stats()

    def _load_stats(self) -> None:
        """Load statistics from the CSV file if it exists."""
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                reader = csv.reader(file)
                next(reader, None)  # Skip header
                for row in reader:
                    self.stats['wins'] = int(row[0])
                    self.stats['losses'] = int(row[1])
                    self.stats['draws'] = int(row[2])

    def update_stats(self, result: str) -> None:
        """Update statistics based on the result."""
        if result == 'Player':
            self.stats['wins'] += 1
        elif result == 'Computer':
            self.stats['losses'] += 1
        else:
            self.stats['draws'] += 1
        self._save_stats()

    def _save_stats(self) -> None:
        """Save the current statistics to the CSV file."""
        with open(self.file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Wins', 'Losses', 'Draws'])
            writer.writerow([self.stats['wins'], self.stats['losses'], self.stats['draws']])

    def get_stats(self) -> str:
        """Return formatted statistics."""
        return f"Wins: {self.stats['wins']}, Losses: {self.stats['losses']}, Draws: {self.stats['draws']}"
