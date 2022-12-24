# these rules test row, column and square and exclude
# possibilities from squares where that value is already
# determined for another square

def processRow(x, a):
    # if already a single value then nothing to do
    if len(a[x]) == 1:
        return a

    # find start of row, end is start + 9
    row = (x // 9) * 9
    #print(f"Processing {a[row:row+9]}")
    for i in range(row, row+9):
        if i == x:
            continue
        if len(a[i]) == 1:
            c = a[i][0]
            # remove from a[x]
            if c in a[x]:
                a[x].remove(c)
                if len(a[x]) == 0:
                    raise Exception(f"Error, removed {c} from index {x}")

    #print(f"Got        {a[row:row+9]}")
    return a




def processSquare(x, a):
    # if already a single value then nothing to do
    if len(a[x]) == 1:
        return a

    # find start of square, sequence is 
    # s, s+1, s+2, s+9, s+10, s+11, s+18, s+19, s+20
    s = ((x // 27) * 27) + (((x % 9) // 3) * 3)
    #print(f"Processing square for element {x} start is {s}")
    seq = [s, s+1, s+2, s+9, s+10, s+11, s+18, s+19, s+20]
    for i in seq:
        #print(f"i is {i}")
        if i == x:
            continue
        if len(a[i]) == 1:
            c = a[i][0]
            # remove from a[x]
            if c in a[x]:
                a[x].remove(c)
                if len(a[x]) == 0:
                    raise Exception(f"Error, removed {c} from index {x}")

    return a


def processColumn(x, a):
    # if already a single value then nothing to do
    if len(a[x]) == 1:
        return a

    # find start of column, subsequent values
    # are col+9, end is col+(9*8)
    col = x % 9
    for i in range(col, col+72+1, 9):
        #print(f"Index {i}")
        if i == x:
            continue
        if len(a[i]) == 1:
            c = a[i][0]
            # remove from a[x]
            if c in a[x]:
                a[x].remove(c)
                if len(a[x]) == 0:
                    prettyPrint.debugPrint(a)
                    raise Exception(f"Error, removed {c} from {i} from index {x}")

    #print(f"Got        {a[row:row+9]}")
    return a
