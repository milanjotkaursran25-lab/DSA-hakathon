N = int(input("N: "))
last = N % 10
while N >= 10:
     N = N // 10
     first = N
print("First:", first)
print("Last:", last)