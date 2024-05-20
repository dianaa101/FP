#  Găsiți cel mai mare număr prim mai mic decât un număr dat. Daca nu exista un astfel de număr,
#  tipăriți un mesaj.

n = input("n: ")
n = int(n)

found = 0
m = n

while m > 1:
    m = m - 1
    prime = True
    for d in range(2, m):
        if m % d == 0:
            prime = False
            break

    if prime:
        found = m
        break

if found == 0:
    print("Not Found")
else:
    print(m)