import timeit

popzero = timeit.Timer("x.pop(0)", "from __main__ import x")

popend = timeit.Timer("x.pop()", "from __main__ import x")

print "pop(0)   pop()"

for i in range(100000, 100000001, 1000000):
    x = list(range(i))
    pt = popend.timeit(number=1000)
    x = list(range(i))
    pz = popzero.timeit(number=1000)
    print "%15.5f, %15.5f" % (pz,pt)
