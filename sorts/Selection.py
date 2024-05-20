def selection_sort(arr):
    for i in range(0, len(arr) - 1):
        current_min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[current_min_index]:
                current_min_index = j
        # SWAP
        arr[i], arr[current_min_index] = arr[current_min_index], arr[i]





arr = [2, 6, 5, 1, 3, 4]
selection_sort(arr)
print(arr)