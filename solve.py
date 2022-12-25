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


def countSquaresComplete(a):
    # Count how many squares out of a possible
    # 81 have been finalised
    count = 0
    for i in range(81):
        if len(a[i]) == 1:
            count += 1

    return count

def applyRules(a):
    # apply rules to a until either complete
    # or no more progress being made

    # if complete then just return
    squaresDone = countSquaresComplete(a)
    if squaresDone == 81:
        return a

    # remember current state to measure progress
    lastSquaresDone = 0
    while squaresDone != 81 and squaresDone != lastSquaresDone:
        # apply rules
        for i in range(81):
            a = rules.processRow(i, a)
            a = rules.processSquare(i, a)
            a = rules.processColumn(i, a)

        lastSquaresDone = squaresDone
        squaresDone = countSquaresComplete(a)

    return a



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

# apply the rules until exhausted
a = applyRules(a)
squaresComplete = countSquaresComplete(a)
print(f"{squaresComplete} squares complete")
prettyPrint.pprint(a)

if squaresComplete != 81:
    prettyPrint.debugPrint(a)

