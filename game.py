from board import Board
from player import Player
from coordinate import Coordinate
from fileStore import FileStore
import os

class Game:
    def __init__(self):
        self.store = FileStore()

        print("Enter Player 1 name:")
        p1 = input("> ")
        print("Enter Player 2 name:")
        p2 = input("> ")

        self.p1 = Player(p1, Board(), Board())
        self.p2 = Player(p2, Board(), Board())

        hs = self.store.get_high_score()
        if hs:
            print(f"\nCurrent High Score: {hs['winner']} with {hs['guesses']} guesses.\n")

    def start(self):
        self.p1.place_fleet()
        self.p2.place_fleet()

        turn = 1
        guess_count = {self.p1.name: 0, self.p2.name: 0}

        while True:
            attacker = self.p1 if turn % 2 == 1 else self.p2
            defender = self.p2 if attacker == self.p1 else self.p1

            print(f"\n{attacker.name}'s Turn")
            print("Enter target (e.g., A5): ")
            guess = input("> ").upper()
            coord = Coordinate.parse(guess)
            if coord is None:
                print("Invalid location.")
                continue

            result, ship_name = defender.board.receive_attack(coord.row, coord.col)

            if result == "INVALID":
                print("Invalid choice.")
                continue
            if result == "REPEAT":
                print("Already guessed.")
                continue

            guess_count[attacker.name] += 1

            if result == "MISS":
                print("MISS.")
            elif result == "HIT":
                print(f"HIT {ship_name}!")
            elif result == "SUNK":
                print(f"{ship_name} SUNK!")

            if defender.all_sunk():
                print(f"\nWINNER: {attacker.name}")
                remaining = sum(not s.is_sunk() for s in attacker.ships)
                self.store.record_game(attacker.name, guess_count[attacker.name], remaining)
                break

            turn += 1
