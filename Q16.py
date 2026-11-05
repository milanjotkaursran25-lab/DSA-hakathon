N = int(input("N: "))
for num in range(2, N + 1):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num)

