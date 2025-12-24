class Coordinate:
    def __init__(self, row, col):
        self.row = row
        self.col = col

    @staticmethod  #using staticmethod as it does not depend on instance state and is utility function
    def parse(cell):
        """
        Example input: 'A5'
        Returns Coordinate(row=0, col=5)
        """
        if len(cell) < 2:
            return None

        row_char = cell[0].upper()
        if not ('A' <= row_char <= 'Z'):
            return None

        try:
            col = int(cell[1:])
        except:
            return None

        return Coordinate(ord(row_char) - 65, col)
