from coordinate import Coordinate
import os

class Player:
    def __init__(self, name, board, guess_board):
        self.name = name
        self.board = board
        self.guess_board = guess_board
        self.ships = []

    def add_ship(self, ship):
        self.ships.append(ship)

    def all_sunk(self):
        return all(s.is_sunk() for s in self.ships)

    def place_fleet(self):
        print(f"\n--- {self.name}: Ship Placement (secret) ---\n")

        fleet_info = [
            ("Destroyer-1", 3),
            ("Destroyer-2", 3),
            ("Cruiser", 5),
            ("Battleship", 7),
            ("Aircraft Carrier", 9),
        ]

        for name, size in fleet_info:
            placed = False
            while not placed:
                print(f"Place {name} (size {size}).")

                orient = input("Enter orientation (H for horizontal, V for vertical): ").upper()
                if orient not in ['H', 'V']:
                    print("Invalid orientation.\n")
                    continue

                mid = input("Enter middle cell (e.g., A5): ").upper()
                coord = Coordinate.parse(mid)
                if coord is None:
                    print("Invalid coordinate.\n")
                    continue

                from ship import Ship
                ship_obj = Ship(name, size)

                if self.board.place_ship_center(ship_obj, coord.row, coord.col, orient):
                    self.add_ship(ship_obj)
                    print(f"{name} placed.\n")
                    placed = True
                else:
                    print("Invalid placement. Try again.\n")

        print("All ships placed!\n")
        input("Press ENTER to continue (hide screen).")
        os.system("cls" if os.name == "nt" else "clear")
