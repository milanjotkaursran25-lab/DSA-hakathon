a = int(input("A:"))
b = int(input("B:"))
while b != 0:
    a, b = b, a % b
print("GCD:", a)










#         n = 153

# temp = n
# digits = len(str(n))
# total = 0

# while temp > 0:
#     digit = temp % 10
#     total += digit ** digits
#     temp //= 10

# if total == n:
#     print("True")
# else:
#     print("False")


#     n = 6
# total = 0

# for i in range(1, n):
#     if n % i == 0:
#         total += i

# if total == n:
#     print("True")
# else:
#     print("False")


#     binary = "1101"

# decimal = int(binary, 2)

# print("Decimal =", decimal)


# n = 13

# binary = bin(n)[2:]

# print("Binary =", binary)