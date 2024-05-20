# Generați cel mai mare număr perfect mai mic decât un număr dat. Daca nu exista un astfel de
# număr, tipăriți un mesaj. Un număr este perfect daca este egal cu suma divizorilor proprii.

n = input("n: ")
n = int(n)

# m - nr. perfect < n
m = n
found = 0

while m > 1:
    m = m - 1
    s = 0
    for i in range(1, m):
        if m % i == 0:
            s = s + i
    if s == m:
        found = m
        break
if found == 0:
    print("Not Found")
else:
    print(m)