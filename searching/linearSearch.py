"""
Linear Search Algorithm
A simple search algorithm that checks each element in a list sequentially
until the target is found or the list is exhausted. Time Complexity: O(n)
"""


def linear_search(arr, target):
    """
    Perform linear search on an array.
    
    Args:
        arr: List of elements (does not need to be sorted)
        target: Element to search for
    
    Returns:
        int: Index of target if found (0-based), -1 otherwise
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


def main():
    """Example usage of linear search."""
    # Example 1: Integer list
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target = 7
    
    print("=" * 50)
    print("Linear Search Algorithm")
    print("=" * 50)
    print(f"\nArray: {lst}")
    print(f"Searching for: {target}")
    
    result = linear_search(lst, target)
    
    if result != -1:
        print(f"✅ Value found at index {result} (position {result + 1})")
    else:
        print("❌ Value not found in the sequence")
    
    # Example 2: Unsorted list
    print("\n" + "-" * 50)
    unsorted_lst = [45, 12, 78, 23, 56, 34, 90, 1]
    target2 = 56
    
    print(f"\nUnsorted array: {unsorted_lst}")
    print(f"Searching for: {target2}")
    
    result2 = linear_search(unsorted_lst, target2)
    
    if result2 != -1:
        print(f"✅ Value found at index {result2} (position {result2 + 1})")
    else:
        print("❌ Value not found in the sequence")
    
    # Example 3: Element not found
    print("\n" + "-" * 50)
    target3 = 99
    print(f"\nArray: {lst}")
    print(f"Searching for: {target3}")
    
    result3 = linear_search(lst, target3)
    
    if result3 != -1:
        print(f"✅ Value found at index {result3}")
    else:
        print("❌ Value not found in the sequence")


if __name__ == "__main__":
    main()
