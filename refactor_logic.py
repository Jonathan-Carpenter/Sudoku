from refactor_cell import Cell, GUICell
from refactor_main import GUISudoku

import random

class Sudoku:
    def __init__(self, difficulty):
        self.difficulty = difficulty

        success = False
        while not success:
            success = self.init_cells()
        self.set_start()

    def init_cells(self):
        self.cells=[[]]*9
        for r in range(9):
            self.cells[r] = []
            for c in range(9):
                if issubclass(self, GUISudoku): cell = GUICell([r,c], self)
                else: cell = Cell([r,c], self)

                try:
                    cell.entry = random.choice(cells.getValids())
                    self.cells.append(cell)
                except:
                    return False

    def set_start(self):
        hidden = random.sample([cell for row in self.cells for cell in row], int(self.difficulty*81))
        for cell in hidden:
            cell.entry = None

    def getRow(self, r):
        return self.cells[r]

    def getCol(self, c):
        return [row[c] for row in self.cells[:r]]

    def getSquare(self, r, c):
        square = []
        for row in self.cells[r-r%3:r-r%3+3]:
            for cell in row[c-c%3:c-c%3+3]:
                square.append(cell)
        return square
