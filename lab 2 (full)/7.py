# Fie n un număr natural dat. Calculați produsul p al tuturor factorilor proprii ai lui n.

n = input("n: ")
n = int(n)
p = 1

for i in range(2, n):
    if n % i == 0:
        p = p * i

print("p: " + str(p))