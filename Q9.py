N = int(input("N: "))
original = N
reverse = 0
while N > 0:
       reverse = reverse * 10 + N % 10 
       N = N // 10
if original == reverse:
      print(True)
else:
       print(False)