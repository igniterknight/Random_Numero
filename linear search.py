import random as rd

def search(y, x):
    l = 0
    while l < 500:
        if x[l] == y:
            return l
        l += 1
    return -1

x = []
for i in range(1,501):
    i = rd.randint(1,999)
    x.append(i)

y = int(input("Write a number ranging 1 to 1000: "))

result = search(y, x)
if (result == -1):
    print("Element doesnt exist.")
else:
    print("Element does exist!")


