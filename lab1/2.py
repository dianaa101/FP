# Verificați daca un număr citit de la tastatura este prim

n = input("n: ")
n = int(n)
prime = True

if n == 1:
    prime = False
else:
    for i in range(2, n):
        if n % i == 0:
            prime = False
            break

if prime:
    print("prime")
else:
    print("not prime")

