# Generați cel mai mic număr perfect mai mare decât un număr dat. Un număr este perfect daca
# este egal cu suma divizorilor proprii. Ex. 6 este un număr perfect (6=1+2+3).

n = input("n: ")
n = int(n)

# m - nr. perfect > n
m = n

while True:
    m = m + 1
    s = 0
    for i in range(1, m):
        if m % i == 0:
            s = s + i
    if s == m:
        break
print(m)
