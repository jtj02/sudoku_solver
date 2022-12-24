# some special characters for printing
B = "|"
DB = "\u2016"
HB = "\u2015"
DHB = "\u2550"

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


def debugPrint(a):
    for y in range(9):
        print(f"{y*9}:", a[y*9:(y*9)+9])
