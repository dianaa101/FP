# Calculați suma a n numere naturale
n = input("n: ")
n = int(n)
s = 0

for _ in range(n):
    x = input("x: ")
    x = int(x)
    s = s + x

print("s: " + str(s))


