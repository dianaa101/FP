def selection_sorted(arr, key=lambda x: x, reverse=False):
    arr = arr[:]

    for i in range(0, len(arr) - 1):
        current_min_index = i
        # gaseste index-ul elementului minim in partea neordonata a array-ului
        for j in range(i + 1, len(arr)):
            if key(arr[j]) < key(arr[current_min_index]):
                current_min_index = j
        # SWAP
        arr[i], arr[current_min_index] = arr[current_min_index], arr[i]
    if reverse:
        arr.reverse()

    return arr


def cocktail_sorted(arr, key=lambda x: x, reverse=False):
    arr = arr[:]

    left = 0
    right = len(arr) - 1

    while left <= right:
        for i in range(left, right):
            if key(arr[i]) > key(arr[i + 1]):
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        right = right - 1

        for i in range(right, left, - 1):
            if key(arr[i - 1]) > key(arr[i]):
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
        left = left + 1

    if reverse:
        arr.reverse()

    return arr
