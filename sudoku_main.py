import tkinter as tk
import argparse
from sudoku_logic import GUISudoku

parser = argparse.ArgumentParser()
parser.add_argument("--difficulty", type=float, default=0.4, help="difficulty value is the proportion of blank cells at the start of the puzzle")
parser.add_argument("--font_size", type=int, default=15)

args = parser.parse_args()

root = tk.Tk()
root.configure(background="black")
sudoku_gui = GUISudoku(root, difficulty=args.difficulty, known_colour="gray87", cell_size=2, font_size=args.font_size)
root.bind("<Key>", lambda e: sudoku_gui.active_cell_entry(e))
root.mainloop()
