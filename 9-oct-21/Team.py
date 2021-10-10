n = int(input())
o = 0
while n > 0:
    a = [int(i) for i in input().split(" ")]
    b = 0
    for i in a:
        if i == 1:
            b+=1
    if b > 1:
        o+=1
    n -= 1
print(o)
