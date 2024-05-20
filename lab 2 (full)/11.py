# Numerele n1 si n2 au proprietatea P daca scrierile lor in baza 10 conțin
# aceleași cifre (ex. 2113 si 323121). Determinați daca doua numere naturale
# au proprietatea P

n1 = input("n1: ")
n1 = int(n1)
c1 = set()

while n1 > 0:
    x = n1 % 10
    n1 = n1 // 10
    c1.add(x)

n2 = input("n2: ")
n2 = int(n2)
c2 = set()

while n2 > 0:
    x = n2 % 10
    n2 = n2 // 10
    c2.add(x)

if c1 == c2:
    print("YES")
else:
    print("NO")
