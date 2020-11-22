import refactor_cell

import random
import tkinter as tk

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
                if isinstance(self, GUISudoku): cell = refactor_cell.GUICell([r,c], self)
                else: cell = refactor_cell.Cell([r,c], self)

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

class GUISudoku(Sudoku):
    def __init__(self, master, cell_size=3, known_colour="gray80", unknown_colour="gray95", updating_colour="sky blue", invalid_colour="tomato", **kwds):
        self.master = master
        self.cell_size = cell_size
        self.known_colour = known_colour
        self.unknown_colour = unknown_colour
        self.updating_colour = updating_colour
        self.invalid_colour = invalid_colour
        self.active_cell = None
        super().__init__(**kwds)

        self.display()

    def display(self):
        for r in range(9):
            for c in range(9):
                self.print_cell(r, c)

    def print_cell(self, r, c, pad_x=0, pad_y=0):
        if r in {3,6}: pad_y = (self.cell_size, 0)
        if c in {3,6}: pad_x = (self.cell_size, 0)

        cell = self.cells[r][c]
        cell.widget = tk.Label(self.master, text=str(cell),
          width=self.cell_size*2, height=self.cell_size,
          borderwidth=2, relief="groove")
        cell.widget.grid(row=r, column=c, padx=pad_x, pady=pad_y)
        cell.widget.bind("<Button-1>", lambda e: self.set_active_cell(cell))
        cell.widget["bg"] = cell.default_colour

    def set_active_cell(self, cell):
        if cell.widget["bg"] == self.known_colour: return

        if self.active_cell != None:
            self.active_cell.set_colour(self.active_cell.default_colour)

        self.active_cell = cell
        cell.set_colour(self.updating_colour)

    def active_cell_entry(self, event):
        if self.active_cell == None or event.char not in "123456789":
            return

        self.active_cell.set_entry(event.char)
