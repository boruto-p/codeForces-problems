a = [int(i) for i in input().split(" ")]
n = a[0]
k = a[1]
k-=1
o = 0
b = [int(i) for i in input().split(" ")]
c = b[k]
for i in b:
    if c != 0:
        if i >= c:
            o += 1
    else:
        if i > c:
            o += 1
print(o)
