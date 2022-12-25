import sys

import input
import prettyPrint
import rules

# Usage
usage = "Usage: " + sys.argv[0] + " [filename]"

def init():
    s = []
    for i in range(81):
        s.append([0,1,2,3,4,5,6,7,8,9])

    return s




# start the program
if len(sys.argv) == 1:
    # get start from user input
    a = input.starting()

if len(sys.argv) == 2:
    # treat command line argument as file with starting data
    a = input.parseFile()

if len(sys.argv) > 2:
    print(usage, file=sys.stderr)
    sys.exit(1)

# have starting point
prettyPrint.pprint(a)

# now the work!
lastSquaresDone = -1
squaresDone = 0
while squaresDone != lastSquaresDone and squaresDone != 81:
    for i in range(81):
        b = rules.processRow(i, a)
        c = rules.processSquare(i, b)
        d = rules.processColumn(i, c)
        a = d

    lastSquaresDone = squaresDone
    squaresDone = 0
    for i in range(81):
        if len(a[i]) == 1:
            squaresDone += 1

    print(f"{squaresDone} squares complete")
    prettyPrint.pprint(d)

prettyPrint.debugPrint(a)

