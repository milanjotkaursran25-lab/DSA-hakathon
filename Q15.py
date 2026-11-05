N = int(input("N: "))
if N <= 1:
    print("Not Prime")
else:
    for i in range(2, N):
        if N % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")