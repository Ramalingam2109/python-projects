"""
Binary Search Algorithm
A divide-and-conquer search algorithm that finds the position of a target value
within a sorted array. Time Complexity: O(log n)
"""


def binary_search(arr, target):
    """
    Perform binary search on a sorted array.
    
    Args:
        arr: Sorted list of elements
        target: Element to search for
    
    Returns:
        int: Index of target if found, -1 otherwise
    """
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1


def main():
    """Example usage of binary search."""
    # Example 1: Integer list
    lst = [4, 7, 8, 12, 45, 99]
    target = 45
    
    print("=" * 50)
    print("Binary Search Algorithm")
    print("=" * 50)
    print(f"\nSorted array: {lst}")
    print(f"Searching for: {target}")
    
    result = binary_search(lst, target)
    
    if result != -1:
        print(f"✅ Element {target} found at index {result}")
    else:
        print(f"❌ Element {target} not found in the array")
    
    # Example 2: String list
    print("\n" + "-" * 50)
    words = ["apple", "banana", "cherry", "date", "elderberry"]
    word_target = "cherry"
    
    print(f"\nSorted array: {words}")
    print(f"Searching for: {word_target}")
    
    result = binary_search(words, word_target)
    
    if result != -1:
        print(f"✅ Element '{word_target}' found at index {result}")
    else:
        print(f"❌ Element '{word_target}' not found in the array")


if __name__ == "__main__":
    main()