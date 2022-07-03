#from sys import stdin

ix = 0
while True:
    try:
        ln = input()
        ix += 1
        print("{}) {}".format(ix, ln))
    except EOFError:
        break
