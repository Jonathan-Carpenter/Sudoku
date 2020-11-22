from refactor_logic import Sudoku
import tkinter as tk

class GUISudoku(Sudoku):
    def __init__(self, master, cell_size=3, known_colour="gray80", unknown_colour="gray95", updating_colour="sky blue", **kwds):
        self.master = master
        self.cell_size = cell_size
        self.known_colour = known_colour
        self.unknown_colour = unknown_colour
        self.updating_colour = updating_colour
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
        self.active_cell = cell

    def update_cell(self, event):
        pass

root = tk.Tk()
sudoku_gui = GUISudoku(root, difficulty=0.7)
root.bind("<Key>", lambda e: sudoku_gui.update_cell(e))
root.mainloop()
