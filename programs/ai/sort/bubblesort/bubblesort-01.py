def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Track whether we made any swaps in this pass
        swapped = False
        for j in range(0, n - i - 1):
            # Swap if the element is greater than the next one
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # If no swaps occurred, the list is already sorted
        if not swapped:
            break
    return arr

# Example usage
numbers = [64, 34, 25, 12, 22, 11, 90]
sorted_numbers = bubble_sort(numbers)
print("Sorted list:", sorted_numbers)
