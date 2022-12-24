import sys

# some special characters for printing
B = "|"
DB = "\u2016"
HB = "\u2015"
DHB = "\u2550"

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
                print(f"{s[i]} ", end="")
        
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

a = init()
#a = starting()
pprint(a)