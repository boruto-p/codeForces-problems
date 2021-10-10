# A. Bear and Big Brother
j = [int(i) for i in input().split(" ")]
a, b, c = j[0], j[1], 0
for i in range(1, 100000000000000):
    a = a*3
    b = b*2
    if a > b:
        c = i
        break
print(c)