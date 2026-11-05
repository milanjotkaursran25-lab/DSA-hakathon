N = int(input("N: "))
total = 0
while N > 0:
       digit = N % 10
       total += digit
       N = N // 10
print(total)