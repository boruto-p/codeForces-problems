k = int(input())
while k > 0:
    j = int(input())
    o = "YES"
    a = input()
    b = input()
    for i in range(1, j):
        if a[i] == "0" or b[i] == "0":
            continue
        else:
            o = "NO"
    print(o)
    k -= 1
