N = int(input("N: "))
total = 0
for i in range(1, N):
    if N % i == 0:
        total += i
if total == N and N > 0:
    print("True")
else:
    print("False")