# sudoku_solver
Python code to solve Sudoku puzzles. Written as a distraction while recovering from surgery. All my own work except for sample Sudoku puzzles (the `.txt` files) that were copied from random web sites to use as tests.


## How to use

Clone repo. Run against sample puzzles, e.g.

`python3 solve.py medium1.txt`

Running without filename argument should prompt you for manual entry of the starting point. Enter as numbers `1` to `9` for known cells and the character `-` for unknown cells, no whitespace inbetween. e.g. a line may look like:

`123---7-9`

The manual entry has not been tested nearly as much as providing a filename argument so you may stumble up against a bug

## Puzzle File Format

Has to be 9 lines with 9 characters per line. No trialing newline at the end.

## Prerequistes

Just needs Python3 no external modules required.

## Author

`jtj02` - for all code

Various web sites - example puzzles
