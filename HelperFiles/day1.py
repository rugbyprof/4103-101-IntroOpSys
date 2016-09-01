import random
import pprint

L = [4,5,6,7,3,4,5,6,7,8]
print(L)

L.append(88)

print(L)

L[4] = 33

print(L)

print(len(L))

L.insert(len(L),99)

L.remove(5)

print(L)

LL = ["banana","red",99,'your momma']
print(LL)

L.append(LL)

print(L)

for x in L:
	if type(x) is list:
		for z in x:
			print(z)
	else:
	    print(x)
	    
My2DList = []

for i in range(10):
	My2DList.append([])
	for j in range(10):
		My2DList[i].append(j)
		


pp = pprint.PrettyPrinter(depth=4)

pp.pprint(My2DList)
