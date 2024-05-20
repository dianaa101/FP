# Găsește cel mai mic număr m din șirul lui Fibonacci definit de
#  f[0]=f[1]=1, f[n]=f[n-1]+f[n-2], pentru n>2,
#  mai mare decât numărul natural n dat, deci exista k astfel ca f[k]=m si m>n

n = input("n: ")
n = int(n)
x = 1
y = 1
found = 0
k = 1

while not found:
    m = x + y
    k = k + 1
    if m > n:
        found = m
        break

    x = y
    y = m

print("m: " + str(m) + ", k: " + str(k))
