# Calculați cel mai mare divizor comun a doua numere
def read_int(s):
    while True:
        x = input(s)
        try:
            x = int(x)
            return x
        except ValueError:
            print("invalid")


a = read_int("a: ")
a = abs(a)
b = read_int("b: ")
b = abs(b)

if a != 0 and b == 0:
    n = a
elif a == 0 and b != 0:
    n = b
else:
    n = min(a, b)
    while n > 0:
        if a % n == 0 and b % n == 0:
            break
        n = n - 1

print("n: " + str(n))
