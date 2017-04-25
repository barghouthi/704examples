from z3 import *

x = BitVec('x', 8)
y = BitVec('y', 8)

h1 = BitVec('h1',8)
h2 = BitVec('h2',8)

phi_s = y == (~(x)) & (x + 1)
phi_s2 = y == (~(x + 14)) & (x + 15)

t1 = And(x == 0, y == 1)
t2 = And(x == 1, y == 2)
t3 = And(x == 2, y == 1)
phi_t = Or(t1,t2,t3)

encoding = ForAll([x,y], Implies(phi_t, phi_s))

s = Solver()
s.add(encoding)
print s.check()
print s.model()
