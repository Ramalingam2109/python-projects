# 🔍 Searching Algorithms

Implementation of fundamental searching algorithms with examples, explanations, and performance analysis. Perfect for learning computer science fundamentals.

## Algorithms Included

### 1. Linear Search (`linearSearch.py`)
- **Time Complexity**: O(n)
- **Space Complexity**: O(1)
- **Best Case**: O(1) - Element found at first position
- **Worst Case**: O(n) - Element not found or at last position
- **Use Case**: Works on any array, sorted or unsorted

### 2. Binary Search (`binarySearch.py`)
- **Time Complexity**: O(log n)
- **Space Complexity**: O(1)
- **Best Case**: O(1) - Element found at middle
- **Worst Case**: O(log n) - Element not found
- **Use Case**: Requires sorted array, much faster than linear search

## Requirements

- Python 3.6 or higher
- No external dependencies (uses only standard library)

## Installation

No installation required! Just download and run the files.

**Note**: This project has a `requirements.txt` file that confirms no external dependencies are needed.

## Usage

### Linear Search

```bash
python linearSearch.py
```

**Example Output**:
```
==================================================
Linear Search Algorithm
==================================================

Array: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Searching for: 7
✅ Value found at index 6 (position 7)
```

### Binary Search

```bash
python binarySearch.py
```

**Example Output**:
```
==================================================
Binary Search Algorithm
==================================================

Sorted array: [4, 7, 8, 12, 45, 99]
Searching for: 45
✅ Element 45 found at index 4
```

## Algorithm Details

### Linear Search

**How it works**:
1. Start from the first element
2. Compare each element with the target
3. If found, return the index
4. If not found after checking all elements, return -1

**Code Structure**:
```python
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
```

**Advantages**:
- Works on unsorted arrays
- Simple to implement
- No preprocessing required

**Disadvantages**:
- Slow for large arrays
- Must check every element in worst case

### Binary Search

**How it works**:
1. Requires a sorted array
2. Compare target with middle element
3. If equal, return index
4. If target is smaller, search left half
5. If target is larger, search right half
6. Repeat until found or array exhausted

**Code Structure**:
```python
def binary_search(arr, target):
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
```

**Advantages**:
- Very fast (O(log n))
- Efficient for large sorted arrays
- Reduces search space by half each iteration

**Disadvantages**:
- Requires sorted array
- More complex than linear search
- Not suitable for unsorted data

## Performance Comparison

| Array Size | Linear Search | Binary Search |
|------------|---------------|---------------|
| 10 elements | 10 comparisons | 4 comparisons |
| 100 elements | 100 comparisons | 7 comparisons |
| 1,000 elements | 1,000 comparisons | 10 comparisons |
| 1,000,000 elements | 1,000,000 comparisons | 20 comparisons |

## When to Use Which?

### Use Linear Search When:
- Array is small (< 100 elements)
- Array is unsorted
- You need to search only once
- Simplicity is important

### Use Binary Search When:
- Array is large (> 1000 elements)
- Array is sorted
- You need to search multiple times
- Performance is critical

## Code Examples

### Example 1: Searching in Integer Array

```python
numbers = [1, 3, 5, 7, 9, 11, 13, 15]
target = 7

# Linear Search
result = linear_search(numbers, target)

# Binary Search (requires sorted array)
result = binary_search(numbers, target)
```

### Example 2: Searching in String Array

```python
words = ["apple", "banana", "cherry", "date"]
target = "cherry"

# Both work on strings
result_linear = linear_search(words, target)
result_binary = binary_search(words, target)
```

## Learning Points

These implementations teach:
- **Algorithm Design**: How to design efficient search algorithms
- **Time Complexity**: Understanding Big O notation
- **Space Complexity**: Analyzing memory usage
- **Problem Solving**: Breaking down problems into steps
- **Code Optimization**: Writing efficient code

## Exercises

Try these exercises to practice:

1. **Modify Linear Search**: Return all indices where target appears
2. **Recursive Binary Search**: Implement binary search recursively
3. **Search in 2D Array**: Extend to search in matrix
4. **Case-Insensitive Search**: Modify for string searches
5. **Search with Custom Comparator**: Add support for custom comparison

## Further Reading

- [Big O Notation](https://en.wikipedia.org/wiki/Big_O_notation)
- [Search Algorithms](https://en.wikipedia.org/wiki/Search_algorithm)
- [Binary Search Tree](https://en.wikipedia.org/wiki/Binary_search_tree)

## License

This project is open source and available for educational purposes.

---

**Master the fundamentals of searching! 🔍**
