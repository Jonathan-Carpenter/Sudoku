import tkinter as tk
from sudoku_logic import GUISudoku

root = tk.Tk()
root.configure(background="black")
sudoku_gui = GUISudoku(root, difficulty=0.2, known_colour="gray87", cell_size=2, font_size=15)
root.bind("<Key>", lambda e: sudoku_gui.active_cell_entry(e))
root.mainloop()
