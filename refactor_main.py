from refactor_logic import Sudoku

class GUISudoku(Sudoku):
    def __init__(self, master, difficulty=0.7, cell_size=3, known_colour="gray90", updating_colour="sky blue"):
        super().__init__(self, difficulty)
        self.master = master
        self.cell_size = cell_size
        self.known_colour = known_colour
        self.updating_colour = updating_colour
        self.active_cell = None

        self.display()

    def display(self):
        for r in range(9):
            for c in range(9):
                self.print_cell(r, c)

    def print_cell(self, r, c, pad_x=0, pad_y=0):
        pass

    def update_cell(self, event):
        pass

root = tk.Tk()
sudoku_gui = GUISudoku(root)
root.bind("<Key>", lambda e: sudoku_gui.update_cell(e))
root.mainloop()
