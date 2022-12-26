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


def deepCopy(a):
    # make a deep copy of a and return it
    b = a.copy()
    for i in range(81):
        b[i] = a[i].copy()

    return b


def check(seq, a):
    # run through sequence of squares and make sure
    # rules have not been violated for assigned squares
    # by checking same number has not been applied more
    # than once
    v = []
    for i in seq:
        if len(a[i]) > 1:
            continue

        # if no possibilities then somethign wrong
        if len(a[i]) == 0:
            return False

        if a[i][0] in v:
            return False

        v.append(a[i][0])
        
    return True


def checkRules(a):
    # assist in debug, see if we have violated any rules
    # check each column
    columns = range(9)
    for col in columns:
        seq = range(col, col+72+1, 9)
        if not check(seq, a):
            return False

    # check each row
    rows = range(0, 81, 9)
    for row in rows:
        seq = range(row, row+9)
        if not check(seq, a):
            return False

    # check each square
    squares = [0, 3, 6, 27, 30, 33, 54, 57, 60]
    for s in squares:
        seq = [s, s+1, s+2, s+9, s+10, s+11, s+18, s+19, s+20]
        if not check(seq, a):
            return False

    return True


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
            # skip if cell finalised
            if len(a[i]) == 1:
                continue

            #print("Before process row")
            #prettyPrint.pprint(a)
            a = rules.processRow(i, a)
            if not checkRules(a):
                raise Exception("Rules violated processing rows")

            #print("Before process square")
            #prettyPrint.pprint(a)
            a = rules.processSquare(i, a)
            if not checkRules(a):
                raise Exception("Rules violated processing squares")

            #print("Before process column")
            #prettyPrint.pprint(a)
            a = rules.processColumn(i, a)
            if not checkRules(a):
                raise Exception("Rules violated processing columns")

            #print("After run through of rules")
            #prettyPrint.pprint(a)

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
# exception thrown if there is no solution
try:
    a = applyRules(a)
except Exception as e:
    print(f"Not solveable: {e.args[0]}")
    prettyPrint.debugPrint(a)
    sys.exit(1)

squaresComplete = countSquaresComplete(a)
print(f"{squaresComplete} squares complete with rule application")
prettyPrint.pprint(a)
prettyPrint.debugPrint(a)

if squaresComplete == 81:
    sys.exit(0)

# guess if not complete
# find cells with more than one possibility
# and guess a value
print("Guessing a single value for an unassigned squares")
for i in range(81):
    if len(a[i]) == 1:
        continue

    v = a[i].copy()
    squaresComplete = 0
    for g in v:
        b = deepCopy(a)
        b[i] = [g]
        try:
            applyRules(b)
        except Exception as e:
            print(f"Not solveable with guess {g} in square {i}: ", end="") 
            print(e.args[0])
            continue
        
        squaresComplete = countSquaresComplete(b)
        if squaresComplete == 81:
            print(f"Guess {g} in square {i} found a solution")
            prettyPrint.pprint(b)
            break
        else:
            print(f"Guess {g} in square {i} not sufficient to find solution")

    if squaresComplete == 81:
        break

if squaresComplete != 81:
    prettyPrint.debugPrint(a)

