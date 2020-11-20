import random as rdm
from sudoku_cell import Cell
from warnings import warn

class Sudoku:
    def __init__(self, difficulty=0.7):
        self.difficulty = difficulty

        success = False
        while(not success):
            success = self.init_cells()
        self.set_start()

    def init_cells(self):
        self.cells = [[]]*9
        for r in range(9):
            self.cells[r] = []
            for c in range(9):
                # Store possible values of current cell
                poss = []
                # Find cells in current column
                column = [row[c] for row in self.cells[:r]]
                square = []
                for row in self.cells[r-r%3:r-r%3+3]:
                    for cell in row[c-c%3:c-c%3+3]:
                        square.append(cell)

                # A val is possible if it doesn't appear in:
                #   1) the current row, or
                #   2) the current column
                for i in range(1,10):
                    if ( Cell(val=i) not in self.cells[r]
                    and  Cell(val=i) not in column
                    and  Cell(val=i) not in square):
                        poss.append(Cell(val=i))

                # Make a random choice from the possible values; add to cells
                try:
                    cell = rdm.choice(poss)
                except:
                    # print("Cell filling failed at row={}, col={}!".format(r, c))
                    return False

                self.cells[r].append(cell)
        return True

    # Hide some cells based on difficulty
    def set_start(self):
        hidden = rdm.sample([cell for row in self.cells for cell in row], int(self.difficulty*81))
        for cell in hidden:
            cell.unreveal()

    def reveal(self):
        for row in self.cells:
            for cell in row:
                cell.reveal()

    def unreveal(self):
        for row in self.cells:
            for cell in row:
                cell.unreveal()
