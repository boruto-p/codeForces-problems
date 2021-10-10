n = int(input())
while n > 0:
    a = input()
    b = len(a)
    if b > 10:
        b = (b - 2)
        b = str(b)
        o = a[0] + b + a[-1]
        int(b)
    else: o = a
    print(o)
    n-=1
