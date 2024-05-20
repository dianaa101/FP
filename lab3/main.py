def read_numbers():
    # read the length of the list
    n = input("n: ")
    n = int(n)

    # initialize an empty list
    li = []
    for i in range(n):
        # read each element of the list
        x = input(str(i) + ": ")
        x = int(x)
        # add it to the list
        li.append(x)
    return li

# are oricare doua elemente consecutive sunt de semne contrare
def secv12(l):
    # store the start and the length of the longest sequence
    best_start = 0
    best_length = 0

    # store the start and the length of the current sequence
    start = 0
    length = 0

    # iterate over the indices of list l
    for i in range(len(l)):
        # if this is the first element of the list OR
        # if this element is >= 0 and the previous element is < 0 OR
        # if this element is < 0 and the previous element is >= 0
        if i == 0 or l[i - 1] < 0 and l[i] >= 0 or l[i - 1] >= 0 and l[i] < 0:
            # increase the length of the current sequence by 1
            length = length + 1

            # if the current sequence is longer than the
            # longest sequence, set the start and length of the longest sequence
            # to the current sequence
            if length > best_length:
                best_start = start
                best_length = length

        else:
            # we have a new sequence
            # set start to the current index, and length to 1
            start = i
            length = 1

    print("start: " + str(best_start))
    print("length: " + str(best_length))
    best_end = best_start + best_length
    sequence = l[best_start:best_end]
    print("sequence: " + str(sequence))
    return sequence

# suma elementelor este egal cu 5
def secv13(l):
    best_start = 0
    best_length = 0

    # iterate over the indices of list l
    for i in range(len(l)):
        # store the start position and length of the current sequence
        start = i
        length = 0
        # store the sum of the current sequence
        s = 0

        for j in range(i, len(l)):
            # add the current element to the sequence
            s = s + l[j]
            length = length + 1

            # if the sum is 5, check if the current sequence is longer than the
            # longest sequence
            if s == 5:
                if length > best_length:
                    best_length = length
                    best_start = start

    print("start: " + str(best_start))
    print("length: " + str(best_length))
    best_end = best_start + best_length
    sequence = l[best_start:best_end]
    print("sequence: " + str(sequence))
    return sequence

# contine doar din numere prime.
def secv4(l):
    # store the start and the length of the longest sequence
    best_start = 0
    best_length = 0

    # store the start and the length of the current sequence
    start = 0
    length = 0

    # iterate over the indices of list l
    for i in range(len(l)):
        # we start with the assumption that the number at l[i] is prime
        prime = True

        # 1 is not prime
        if l[i] == 1:
            prime = False
        else:
            for d in range(2, l[i]):
                # if we found that the number at l[i] is divisible by any number in the range [2, l[i])
                # then l[i] is not prime
                if l[i] % d == 0:
                    # set prime to false
                    prime = False
                    # stop checking any other divisor
                    break

        # if the number is prime
        if prime:
            # and the current sequence has length 0
            if length == 0:
                # then this is where we start our current sequence
                # set the start to the current index in the list
                start = i

            # increase the length of the current sequence
            length = length + 1

            # check if the length of the current sequence is
            # bigger than the length of our longest sequence
            if length > best_length:
                best_length = length
                best_start = start
        # if the number is not prime
        else:
            # set length to 0 for the next sequence
            length = 0

    print("start: " + str(best_start))
    print("length: " + str(best_length))
    best_end = best_start + best_length
    sequence = l[best_start:best_end]
    print("sequence: " + str(sequence))
    return sequence


assert(secv4([1, 3, 5, 8, 7, 5, 3, 3]) == [7, 5, 3, 3])
assert(secv4([1, 3, 3, 5, 5, 5, 8, 7, 5, 3, 3]) == [3, 3, 5, 5, 5])

l = []

while True:
    print("1. Read numbers")
    print("2. Are oricare doua elemente consecutive de semne contrare")
    print("3. Suma elementelor este egala cu 5")
    print("4. Contine doar numere prime")
    print("5. Exit")
    o = input("o: ")
    if o == "1":
        l = read_numbers()
    elif o == "2":
        secv12(l)
    elif o == "3":
        secv13(l)
    elif o == "4":
        secv4(l)
    elif o == "5":
        break



