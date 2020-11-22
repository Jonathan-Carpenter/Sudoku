Welcome!

This is a Sudoku game made using the `tkinter` Python library. The game generates a random Sudoku and then makes a number of randomly chosen cells blank to start the puzzle.

The number of cells made blank is a proportion of the total, set by the difficulty value, i.e. a value of 0 means that the puzzle is already solved, while a value of 1 means that all cells are blank.

Download all source files and run `sudoku_main.py`. To change the difficulty, run `sudoku_main.py --difficulty <val>`.

Instructions:
- As per the rules of Sudoku, each cell needs to be filled with a number 1-9 such that no row, column or 3x3 square contains duplicate numbers.
- Click on a cell and press a number key to insert that number in that cell. (Cells which were filled from the start cannot be changed.)
- Click on a cell and press the '0' key to remove a number which you inserted there.
- Entering a clearly invalid number (i.e. row, column or square contains that number already) results in a temporary red highlight for that cell, and the number will be removed.
- Have fun! (P.S.: Make sure you finish the game for nice victory animation!)
