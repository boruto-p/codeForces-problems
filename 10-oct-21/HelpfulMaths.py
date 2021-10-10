# A. Helpful Maths
b =[int(i) for i in input().split("+")]
b.sort()
c = ""
for i in b:
    i = str(i)
    c = c + i + "+"
c=c[:-1]
print(c)
