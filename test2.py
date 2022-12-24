import sys
import fileinput

# some special characters for printing
B = "|"
DB = "\u2016"
HB = "\u2015"
DHB = "\u2550"

# Usage
usage = "Usage: " + sys.argv[0] + " [filename]"

a = []

def init():
    s = []
    for i in range(81):
        s.append([0,1,2,3,4,5,6,7,8,9])

    return s

def pprint(s):
    for y in range(9):
        if y % 3 == 0:
            if y == 0:
                print(DHB * 37)
            else:
                print(DB + DHB * 35 + DB)
        else:
            print((DB + HB * 3 + B + HB * 3 + B + HB * 3) * 3 + DB)
        for x in range(9):
            if x % 3 == 0:
                print(f"{DB} ", end="")
            else:
                print(f"{B} ", end="")

            i = (y*9) + x
            if len(s[i]) != 1:
                print("x ", end="")
            else:
                print(f"{s[i][0]} ", end="")
        
        print(DB)

    print(DHB * 37)


def parseRow(r):
    if len(r) != 9:
        print(f"Error, incorrect number of characters for a line, need 9 you entered {len(r)}", file=sys.stderr)
        return []
    
    o = []
    for i in range(9):
        o.append([1,2,3,4,5,6,7,8,9])
        #print(f"so far {o}")
        c = r[i]
        if c == "-":
            continue

        if c.isdigit():
            n = int(c)
            if n >= 1 or n <= 9:
                o[i] = [n]
                continue

        # get to here and we could not parse character
        print(f"Could not parse character {c} in row {r}", file=sys.stderr)
        return []

    # row parse, return output
    return o


def starting():
    print(f"Enter each row of the starting point")
    print("Use a '-' character to indicate an empty square")
    print("Do not enter a space between elements, e.g. a valid line is '1-6-3---5'")

    # input parse and built into this array
    s = []
    for y in range(9):
        
        # Ask for one row at a time, repeat row if cannot parse input
        parsed = False
        while parsed == False:
            xrow = input(f"Enter row {y+1}: ")
            row = parseRow(xrow)
            if len(row) == 9:
                parsed = True

        #print(f"Entered {row}")
        for x in range(9):
            s.append(row[x])

        print(f"row parsed as {s[(y*9):(y*9)+9]}")

    # have all rows
    return s


def parseFile():
    a = []
    for line in fileinput.input():
        row = parseRow(line.strip())
        if len(row) != 9:
            print(f"Error, could not parse line {line.strip()}", file=sys.stderr)
            sys.exit(1)
        
        for x in range(9):
            a.append(row[x])

    if len(a) != 81:
        print("Error parsing file", file=sys.stderr)

    return a


def processRow(x, a):
    # if already a single value then nothing to do
    if len(a[x]) == 1:
        return a

    # find start of row, end is start + 9
    row = (x // 9) * 9
    print(f"Processing {a[row:row+9]}")
    for i in range(row, row+9):
        if i == x:
            continue
        if len(a[i]) == 1:
            c = a[i][0]
            # remove from a[x]
            if c in a[x]:
                a[x].remove(c)

    print(f"Got        {a[row:row+9]}")
    return a


def processSquare(i, a):
    return a


def processColumn(x, a):
    # if already a single value then nothing to do
    if len(a[x]) == 1:
        return a

    # find start of column, subsequent values
    # are col+9, end is col+(9*8)
    col = x % 9
    #print(f"Processing {a[row:row+9]}")
    for i in range(col, col+72+1, 9):
        print(f"Index {i}")
        if i == x:
            continue
        if len(a[i]) == 1:
            c = a[i][0]
            # remove from a[x]
            if c in a[x]:
                a[x].remove(c)

    #print(f"Got        {a[row:row+9]}")
    return a



# start the program
if len(sys.argv) == 1:
    # get start from user input
    a = starting

if len(sys.argv) == 2:
    # treat command line argument as file with starting data
    a = parseFile()

if len(sys.argv) > 2:
    print(usage, file=sys.stderr)
    sys.exit(1)

# have starting point
pprint(a)

# now the work!

for i in range(81):
    b = processRow(i, a)
    c = processSquare(i, b)
    d = processColumn(i, c)
    a = d

pprint(d)