a = int(input())
x = 0
while a > 0:
    b = input()
    o = 0
    for i in b:
        if i == '+':
            o += 1

        if i == '-':
            o -= 1
    if o > 1:
        x += 1
    if o < 0:
        x -= 1
    a -= 1
print(x)
