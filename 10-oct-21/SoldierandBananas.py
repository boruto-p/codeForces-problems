# 546A - Soldier and Bananas
j = [int(i) for i in input().split(" ")]
k, n, w = j[0], j[1], j[2]
o = 0
for i in range(1, w+1):
    o = o + i*k

if o > n:
    print(o-n)
else:print(0)
