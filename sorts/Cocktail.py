def cocktail_sort(arr):
    left = 0
    right = len(arr) - 1

    while left <= right:
        for i in range(left, right):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        right = right - 1

        for i in range(right, left, - 1):
            if arr[i - 1] > arr[i]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
        left = left + 1

arr = [2, 6, 7, 4, 1, 8, 5, 3]
cocktail_sort(arr)
print(arr)