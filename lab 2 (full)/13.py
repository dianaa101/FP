#  Determinați al n-lea element al șirului
#  1,2,3,2,2,5,2,2,3,3,3,7,2,2,3,3,3,...
#  obținut din șirul numerelor naturale prin înlocuirea numerelor compuse prin
#  divizorii lor primi, fiere divizor prim d repetându-se de d ori, fără
#  a retine termenii șirului!

n = input("n: ")
n = int(n)

# the number we found
found = 0

if n == 0:
    # on 0th position of the sequence we have element 1
    found = 1
else:
    # to find the element on the nth position, start from 2 and go up until pos == n
    poz = 0
    val = 1

    # while we haven't found the element nth position
    while found == 0:
        # add 1 to the value of the number we are currently decomposing
        val = val + 1

        # copy the value of the number we are currently decomposing into its prime divisors (starting from 2)
        copy = val

        # iterate over numbers in range [2, copy] to find which one copy is divisible with
        for d in range(2, copy + 1):
            # if copy is not divisible d
            if copy % d != 0:
                # skip to the next d
                continue

            # add d times times
            if d == val:
                times = 1
            else:
                times = d

            for _ in range(times):
                # add 1 to the value of the current position
                poz = poz + 1

                # the current position is equal to n, d is our nth element
                if poz == n:
                    found = d
                    # break out of the divisors loop
                    break

            # while copy is still divisible with d
            while copy % d == 0:
                # divide copy by d
                copy = copy / d

            # we're done with this number
            if copy == 1:
                # break out of the divisors loop
                break

print(found)
