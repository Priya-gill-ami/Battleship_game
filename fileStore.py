import json
import os

class FileStore:
    FILE_NAME = "battleship_scores.json"

    def __init__(self):
        if not os.path.exists(self.FILE_NAME):
            with open(self.FILE_NAME, "w") as f:
                json.dump([], f)

    def record_game(self, winner, guesses, remaining_ships):
        with open(self.FILE_NAME, "r") as f:
            data = json.load(f)

        data.append({
            "winner": winner,
            "guesses": guesses,
            "remaining_ships": remaining_ships
        })

        with open(self.FILE_NAME, "w") as f:
            json.dump(data, f, indent=4)

    def get_high_score(self):
        with open(self.FILE_NAME, "r") as f:
            data = json.load(f)

        if not data:
            return None

        return min(data, key=lambda x: x["guesses"])
