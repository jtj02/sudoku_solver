# sudoku_solver

Python code to solve Sudoku puzzles. Written as a distraction while recovering from surgery. All my own work.

## How to use

Clone repo. Run against sample puzzles (that you can easily find in Internet):

`python3 solve.py example-puzzle.txt`

Running without filename argument should prompt you for manual entry of the starting point. 

## Puzzle File Format

Puzzle format consists of 9 characters per line with numerals `1` to `9` for known cells and the character `-` for unknown cells, no whitespace between characters. e.g. a line may look like:

`123---7-9`

There should be no trailing newline at the end of the file

The manual entry has not been tested nearly as much as providing a filename argument so you may stumble up against a bug

## How It Works

Each unknown cell is initially assumed to possibly contain all 9 digits which are saved as an array `[1,2,3,4,5,6,7,8,9]`. The cells themselves are stored as a one dimensional array row by row, e.g. top left is index `0`, top right in index `9` and bottom left is index `72`. An assigned cell is one where only one possibility remains and will be ar array of length one only containing the assigned value.

The code iterates through each cell applying two rules:

1. if a cell in the same row, column or square is already assigned a number then that cell cannot be that number, the number is removed from the array of possibilities

1. if a cell in the same row, column or square is the only one that could possibly contain a value then it must be that value and the other values are removed from the array of possibilities

If the starting point for the puzzle is incorrect then it is possible that after applying the rules we are left with board that does not have a valid solution. The board is checked and an exception thrown if the solution is invalid.

After applying the simple rules above some puzzles are not completely solved. Rather than applying more complex rules the code proceeds to guess a possible value for an un-assigned cell and then apply the rules further to solve. If the guess does not work the code guesses again. On all puzzles I have tested against repeated trying with a single guess is sufficient to eventually find a solution.

## Prerequisites

Just needs Python3 no external modules required.

## Author

`jtj02` - for all code
