# these rules test row, column and square to work out if
# a square is the only one that could hold a given value

def only(seq, x, a):
    return a

        # what to do

def subtraction(seq, x, a):
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


def processRow(x, a):
    # if already a single value then nothing to do
    if len(a[x]) == 1:
        return a

    # find start of row, end is start + 9
    row = (x // 9) * 9
    seq = range(row, row+9)

    a = subtraction(seq, x, a)
    a = only(seq, x, a)
    return a

def processColumn(x, a):
    # if already a single value then nothing to do
    if len(a[x]) == 1:
        return a

    # find start of column
    col = x % 9
    seq = range(col, col+72+1, 9)

    a = subtraction(seq, x, a)
    a = only(seq, x, a)
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

    a = subtraction(seq, x, a)
    a = only(seq, x, a)
    return a
