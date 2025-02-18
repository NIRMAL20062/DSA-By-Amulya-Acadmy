def hoare_partition(arr, low, high):
    pivot = arr[low]  # First element as pivot
    i, j = low - 1, high + 1  

    while True:
        while True:
            i += 1
            if arr[i] >= pivot:
                break
        while True:
            j -= 1
            if arr[j] <= pivot:
                break

        if i >= j:
            return j

        arr[i], arr[j] = arr[j], arr[i]  # Swap elements

def quick_sort(arr, low, high):
    if low < high:
        pivot_index = hoare_partition(arr, low, high)

        quick_sort(arr, low, pivot_index)
        quick_sort(arr, pivot_index + 1, high)

# Example usage
arr = [10, 7, 8, 9, 1, 5]
quick_sort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)
