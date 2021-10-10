# A. Stones on the Table
n = int(input())
a = input()
k,j = "",0
for i in a:
    if i == k:
        j+=1
    if k != i:
        k = i
print(j)