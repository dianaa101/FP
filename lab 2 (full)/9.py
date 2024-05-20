# Palindromul unui număr este numărul obținut prin scrierea cifrelor in ordine inversa

n = input("n: ")
n = int(n)
c = []

while n > 0:
    x = n % 10
    n = n // 10
    c.append(x)

m = 0
for i in c:
    m = m * 10 + i

print(m)