n = int(input("Enter the number : "))
n1 = n
list1 = []

while n != 0:
    list1.append(n%10)
    n = n // 10

p = len(list1)
sum = 0
for i in range (p):
    sum = sum + (list1[i]**p)

if n1 == sum:
    print(n1, " is Armstrong Number.")
else:
    print(n1, " is not Armstrong Number.")