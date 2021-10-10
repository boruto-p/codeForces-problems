# A. Wrong Subtraction
j=[int(i) for i in input().split(" ")]
a,b = j[0],j[1]
o = a
for i in range(1, b+1):
    c = str(a)
    if c[-1] == "0":
        a = a//10
    else:a -= 1
print(a)
