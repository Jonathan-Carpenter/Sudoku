import tkinter as tk
from refactor_logic import GUISudoku

root = tk.Tk()
sudoku_gui = GUISudoku(root, difficulty=0.7)
root.bind("<Key>", lambda e: sudoku_gui.active_cell_entry(e))
root.mainloop()
