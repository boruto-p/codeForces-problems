# Words
a = input()
u = 0
l = 0
for i in a:
    if i.isupper():
        u += 1

    if i.islower():
        l += 1
if u > l:
    a=a.upper()
else:a=a.lower()
print(a)