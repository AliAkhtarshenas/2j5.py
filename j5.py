import random
n = int(input("enter number:"))
a = []
while len(a) < n:
    x = random.randint(0, n+1)
    if x not in a:
        a.append(x)
print(a)

list = []
a = int(input())
for i in range(a):
    b = int(input("enter the number:"))
    list.append(b)
for i in range(1,len(list)):
    if a[i]<a[i-1]:
        print("no!!!")
        exit()
print("yes")


n = int(input("enter the number:"))
for i in range(n):
    if (i%2)==1:
        print("*", end="")
    else:
        print("#", end="")