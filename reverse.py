num=1234
i=0
while num > 0:
    a=num % 10 #4 -> 3 -> 2 -> 1
    i=i * 10 + a#4 -> 43 -> 432 -> 4321
    num=num // 10
print(i)