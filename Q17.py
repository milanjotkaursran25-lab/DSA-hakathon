N = int(input("N: "))
temp = N
digits = len(str(N))
total = 0
while temp > 0:
    digit = temp % 10
    total += digit ** digits
    temp //= 10
if total == N:
    print("True")
else:
    print("False")