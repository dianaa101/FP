#  Găsiți primul număr prim mai mare decât un număr dat.

n = input("n: ")
n = int(n)

if n < 1:
    n = 1

found = 0

while not found:
    n = n + 1

    prime = True
    for d in range(2, n):
        if n % d == 0:
            prime = False
            break

    if prime:
        found = n
        break

print("found: " + str(found))
