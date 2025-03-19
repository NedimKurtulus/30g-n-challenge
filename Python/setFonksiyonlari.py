setA = {1,2,3,4,5}
setB = {1,3,4,6,7,8}

print(setA | setB )
print(setA.union(setB))
print(setB.union(setA))

print(setA & setB )
print(setA.intersection(setB))
print(setB.intersection(setA))

print(setA - setB )
print(setB - setA )
print(setA.difference(setB))
print(setB.difference(setA))
# simetrik fark kesişimin verdiği kısmın olmadığı union dır 
print(setA ^ setB )
print(setB ^ setA )
print(setA.symmetric_difference(setB))
print(setB.symmetric_difference(setA))
# aynısını verir


