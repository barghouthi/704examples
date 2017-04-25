from z3 import *

x = BitVec('x',8)
y = BitVec('y',8)
h = BitVec('h',8)

phi_n = y == x * 2
phi_s = y == x << h

# first encode the universally quantified formula
encoding = form = ForAll([x,y], phi_n == phi_s) # the == is iff

# now call Z3
s = Solver()
s.add(encoding)

# check if there is a model
s.check()

# print the model (i.e., the value of h)
print s.model()

