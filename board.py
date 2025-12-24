from coordinate import Coordinate

class Board:
    ROWS = 26
    COLS = 10

    def __init__(self):
        self.grid = [[' ' for _ in range(Board.COLS)] for _ in range(Board.ROWS)]
        self.ships = []

    def valid_coord(self, row, col):
        return 0 <= row < Board.ROWS and 0 <= col < Board.COLS

    def place_ship_center(self, ship, mid_row, mid_col, orientation):
        half = ship.size // 2

        cells = []
        if orientation == 'H':
            for c in range(mid_col - half, mid_col + half + 1):
                if not self.valid_coord(mid_row, c):
                    return False
                if self.grid[mid_row][c] != ' ':
                    return False
                cells.append((mid_row, c))

        elif orientation == 'V':
            for r in range(mid_row - half, mid_row + half + 1):
                if not self.valid_coord(r, mid_col):
                    return False
                if self.grid[r][mid_col] != ' ':
                    return False
                cells.append((r, mid_col))

        for r, c in cells:
            self.grid[r][c] = 'S'

        ship.coordinates = cells
        self.ships.append(ship)
        return True

    def receive_attack(self, r, c):
        if not self.valid_coord(r, c):
            return "INVALID", None

        if self.grid[r][c] == 'X' or self.grid[r][c] == '0':
            return "REPEAT", None

        if self.grid[r][c] == 'S':
            self.grid[r][c] = 'X'

            for ship in self.ships:
                if (r, c) in ship.coordinates:
                    ship.register_hit()
                    if ship.is_sunk():
                        return "SUNK", ship.name
                    return "HIT", ship.name

        self.grid[r][c] = '0'
        return "MISS", None
