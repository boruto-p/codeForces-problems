j = input()
s = input()
a=0
d=0
for i in s:
    if i == "D":
        d += 1
    else:
        a += 1
if a > d:
    print("Anton")
if a < d:
    print("Danik")
else:
    print("Friendship")
