from array import *

vals = array('i', [5, 9, 8, 4, 2])

newArr = array(vals.typecode, (a * a for a in vals))

vals = array('u', ['a', 'e', 'i', 'o', 'u'])

for i in range(len(vals)):
    print(vals[i])

for e in newArr:
    print(e)

i = 0
while i < len(newArr):
    print(newArr[i])
    i += 1
