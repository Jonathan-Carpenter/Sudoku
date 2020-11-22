from refactor_cell import Cell, GUICell
import refactor_cell

import random

class Sudoku:
    def __init__(self, difficulty=0.7):
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
                # print("\nSetting cell {}...".format((r,c)))
                if isinstance(self, Sudoku): cell = Cell([r,c], self)
                else: cell = GUICell([r,c], self)

                try:
                    cell.entry = random.choice(cell.getValids())
                except:
                    return False
                self.cells[r].append(cell)
        return True

    def set_start(self):
        hidden = random.sample([cell for row in self.cells for cell in row], int(self.difficulty*81))
        for cell in hidden:
            cell.entry = None
            cell.default_colour = cell.master.unknown_colour

    def getRow(self, r):
        # print("Getting row {}...".format(r))
        return self.cells[r]

    def getCol(self, r, c):
        # print("Getting col {}...".format(c))
        return [row[c] for row in self.cells[:r]]

    def getSquare(self, r, c):
        # print("Getting square at {}...".format((r,c)))
        square = []
        for row in self.cells[r-r%3:r-r%3+3]:
            for cell in row[c-c%3:c-c%3+3]:
                square.append(cell)
        return square
