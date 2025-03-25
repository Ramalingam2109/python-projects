def bubble_sort(arr):
    """
    Sorts a list in ascending order using Bubble Sort.
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    n = len(arr)
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                # Swap if current element is greater than next
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Example Usage
if __name__ == "__main__":
    data = [64, 34, 25, 12, 22, 11, 90]
    print("Original Array:", data)
    sorted_data = bubble_sort(data.copy())
    print("Sorted Array (Bubble Sort):", sorted_data)