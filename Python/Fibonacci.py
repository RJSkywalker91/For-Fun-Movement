import time
import math

def FS(x):
  if x == 1:
    return 1
  elif x == 2:
    return 1
  else:
    return FS(x-1)+FS(x-2)

def FS_robert(x):
    last2 = 1
    last = 1
    current = 1
    if x in [1,2]:
        return 1
    for i in range(2,x):
        current = (last + last2)
        last2 = last
        last = current
    return current

def FS_josh(x, hashmap):
  if x > 2:
    if hashmap.has_key(x-1) == False:
      value1 = FS_josh(x-1, hashmap)
      hashmap[x-1] = value1
    if hashmap.has_key(x-2) == False:
      value2 = FS_josh(x-2, hashmap)
      hashmap[x-2] = value2
    return hashmap[x-1] + hashmap[x-2]
  else:
    hashmap[x] = 1
    return 1


def FS_josh2(x, hashmap):
    #try:
    if hashmap.has_key(x):
      return hashmap[x]
    if hashmap.has_key(x-1):
      value1, value2 = hashmap[x-1]
      sum = value1 + value2
      #hashmap[x] = (sum, value1)
      #return (sum, value1)
      hashmap[x] = (sum+value1, sum)
      return (sum+value1, sum)
    #except:
    else:
      if x == 2:
        hashmap[x] = (2,1)
        hashmap[x-1] = (1,1)
        return 2,1
      else:
    #if hashmap.has_key(x-1) == False:
      #print ("iteration x: {}".format(x))
        value1, value2 = FS_josh2(x-1, hashmap)
        sum = value1 + value2
      #print ("    keys: {}".format(hashmap.keys()))
      #print ("    val1: {}  val 2: {}".format(value1, value2))
      #hashmap[x-1] = (value1, value2)
        hashmap[x] = (sum, value1)
        return (sum, value1)
    #if hashmap.has_key(x-2) == False:
    #  value2 = FS_josh2(x-2, hashmap)
    #  hashmap[x-2] = value2
    #hashmap[x] = hashmap[x-1] + hashmap[x-2]
    #print ("  rval: {}  (added to keys)".format(rval))
    #hashmap[x] = rval
    #return hashmap[x-1] + hashmap[x-2]
    #print ("return F({})={}".format(x, rval[0]))

  #else:
    #hashmap[x] = 15
    #return 1

def FS_three(x):
    if x == 3:
        return 2,1
    else:
        a,b = FS_three(x-1)
        return a+b, a
        #c,d = FS_three(x-2)
        #return (a+b),(c+d)


def FS_square(x):
    phi = (1 + math.sqrt(5)) / 2;
    return round(pow(phi, x) / math.sqrt(5));



if __name__ == "__main__":
    while 1==1:
        value = input("Pick the nth letter of the fibonacci sequence: ")
        hashmap = {}
        hashmap2 = {}
        dict = {}

        print "\nFS_robert function"
        begin5 = time.time()
        x = FS_robert(int(value))
        print "x: {}".format(x)
        end5 = time.time()
        print round(end5-begin5,8)

        #print "\nFirst FS function"
        #begin1 = time.time()
        #print (FS(int(value)))
        #end1 = time.time()
        #print round(end1-begin1,8)

        print "\nFS_Josh function"
        begin2 = time.time()
        x = FS_josh(int(value), hashmap)
        print "x: {}".format(x)
        end2 = time.time()
        print round(end2-begin2,8)

        print "\nFS_three function"
        begin3 = time.time()
        x,y = FS_three(int(value-1))
        print "x: {}".format(x+y)
        end3 = time.time()
        print round(end3-begin3,8)

        #print "\nFourth FS function"
        #begin4 = time.time()
        #x,y = FS_josh2(int(value), hashmap2)
        #print "x: {}".format(x)
        #end4 = time.time()
        #print round(end4-begin4,8)

        print "\nFS_square function"
        begin6 = time.time()
        x = FS_square(int(value))
        print "x: {}".format(x)
        end6 = time.time()
        print round(end6-begin6,8)
