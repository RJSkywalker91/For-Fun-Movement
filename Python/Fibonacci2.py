import time

def optimized(x):
    if x == 1:
        return 1,0
    elif x == 0:
        return 0,0
    a,b = optimized(x-1)
    return a+b, a


if __name__ == "__main__":
    while 1==1:
        val = input("Pick the nth letter of the fibonacci sequence: ")

        print "\nOptimized function"
        start = time.time()
        x,y = optimized(int(val))
        end = time.time()
        print "F({}) = {} took {} seconds".format(val, x, round(end-start,8))
        print "\n"
