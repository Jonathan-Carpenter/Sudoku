import tkinter as tk
from tkinter import ttk
from sudoku_logic import Sudoku

class SudokuGUI:
    def __init__(self, master, cell_size=3, known_colour="gray90", updating_colour="sky blue"):
        self.master = master
        self.cell_size = cell_size
        self.known_colour = known_colour
        self.updating_colour = updating_colour
        self.sudoku = Sudoku()
        # Store the most recently clicked cell
        self.updating = None

        self.display()

    def display(self):
        for r in range(9):
            for c in range(9):
                self.print_cell(r,c)

    def print_cell(self, r, c, pad_x=0, pad_y=0):
        if r in {3,6}: pad_y = (self.cell_size, 0)
        if c in {3,6}: pad_x = (self.cell_size, 0)

        cell = tk.Label(self.master, text=str(self.sudoku.cells[r][c]),
          width=self.cell_size*2, height=self.cell_size,
          borderwidth=2, relief="groove")
        cell.grid(row=r, column=c, padx = pad_x, pady = pad_y)
        cell.bind("<Button-1>", lambda e: self.set_updating(e, self.sudoku.cells[r][c]))

        if self.sudoku.cells[r][c].revealed == True: cell["bg"] = self.known_colour

    def update_cell(self, event):
        if self.updating == None or event.char not in "123456789":
            return

        self.updating[0].enter(int(float(event.char)))
        self.updating[1]["text"] = event.char
        self.updating[1]["bg"] = self.updating[2]
        self.updating = None

    def set_updating(self, event, cell):
        if cell.revealed == True: return

        if self.updating != None:
            self.updating[1]["bg"] = self.updating[2]

        self.updating = (cell, event.widget, event.widget["bg"])
        self.updating[1]["bg"] = self.updating_colour

root = tk.Tk()
sudoku_gui = SudokuGUI(root, cell_size=3)
root.bind("<Key>", lambda e: sudoku_gui.update_cell(e))
root.mainloop()
