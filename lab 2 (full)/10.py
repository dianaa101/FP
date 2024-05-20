#  Pentru un număr natural n dat găsiți numărul natural minim m format cu aceleași cifre.

n = input("n: ")
n = int(n)
c = []

while n > 0:
    x = n % 10
    n = n // 10
    c.append(x)

c.sort()

m = 0
for i in c:
    m = m * 10 + i

print(m)
