

L = ("hi", "hey", "hello", "bye")
M = ("bye", "see ya", "goodbye", "hi")

tup1 = (1,3,5)
tup2 = [value for value in L]
tup3 = [value for value in M]

print(M + L)
print(tup3[-4])
print(5 in tup1)
print(L[-3])
print(tup2.extend([tup3]))
