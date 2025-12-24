class Ship:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.hits = 0
        self.coordinates = []  # will be filled after placement

    def register_hit(self):
        self.hits += 1

    def is_sunk(self):
        """Return True if ship is sunk."""
        return self.hits >= self.size
