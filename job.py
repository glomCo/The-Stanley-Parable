#please don't steal 
#Ben Kreger 2014
import random
import string
import time
l = []
old = 0.0
now = 0
while 1:
    print float(time.time())
    old = int(time.time())
    e = random.choice(string.ascii_letters).lower()
    print "Press " + e
    q = raw_input(">")
    if q == "stats":
            print"average time:" + str(sum(l)/len(l))
            print l
    if q != e:
            print"You had one job!"
            l.extend([float(time.time()) - old])
    else:
            l.extend([float(time.time()) - old])
            
