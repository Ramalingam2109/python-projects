# 📊 Sorting Algorithms

Implementation of classic sorting algorithms with performance analysis, examples, and educational explanations. Perfect for understanding fundamental computer science concepts.

## Algorithms Included

### 1. Bubble Sort (`bubble_sort.py`)
- **Time Complexity**: O(n²)
- **Space Complexity**: O(1)
- **Best Case**: O(n) - Already sorted
- **Worst Case**: O(n²) - Reverse sorted
- **Stability**: Stable
- **Use Case**: Educational purposes, small arrays

### 2. Selection Sort (`selection_sort.py`)
- **Time Complexity**: O(n²)
- **Space Complexity**: O(1)
- **Best Case**: O(n²) - Always same
- **Worst Case**: O(n²) - Always same
- **Stability**: Unstable
- **Use Case**: Educational purposes, small arrays

## Requirements

- Python 3.6 or higher
- No external dependencies (uses only standard library)

## Installation

No installation required! Just download and run the files.

**Note**: This project has a `requirements.txt` file that confirms no external dependencies are needed.

## Usage

### Bubble Sort

```bash
python bubble_sort.py
```

**Example Output**:
```
Original Array: [64, 34, 25, 12, 22, 11, 90]
Sorted Array (Bubble Sort): [11, 12, 22, 25, 34, 64, 90]
```

### Selection Sort

```bash
python selection_sort.py
```

**Example Output**:
```
Original Array: [64, 34, 25, 12, 22, 11, 90]
Sorted Array (Selection Sort): [11, 12, 22, 25, 34, 64, 90]
```

## Algorithm Details

### Bubble Sort

**How it works**:
1. Compare adjacent elements
2. Swap if they are in wrong order
3. Repeat for all pairs
4. After each pass, largest element "bubbles" to the end
5. Continue until no swaps needed

**Visualization**:
```
Pass 1: [64, 34, 25, 12, 22, 11, 90]
        [34, 64, 25, 12, 22, 11, 90]  (swap 64 and 34)
        [34, 25, 64, 12, 22, 11, 90]  (swap 64 and 25)
        ...
        [34, 25, 12, 22, 11, 64, 90]  (90 already in place)

Pass 2: [25, 12, 22, 11, 34, 64, 90]
...
```

**Code Structure**:
```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
```

**Advantages**:
- Simple to understand and implement
- Stable (maintains relative order)
- In-place sorting (O(1) space)
- Adaptive (can detect sorted array)

**Disadvantages**:
- Very slow for large arrays
- O(n²) time complexity
- Many unnecessary comparisons

### Selection Sort

**How it works**:
1. Find minimum element in unsorted portion
2. Swap with first element of unsorted portion
3. Move boundary of sorted portion one position right
4. Repeat until array is sorted

**Visualization**:
```
[64, 34, 25, 12, 22, 11, 90]
 ^                    ^
 |                    |
 Find min (11) and swap with 64

[11, 34, 25, 12, 22, 64, 90]
      ^
      |
 Find min (12) in remaining and swap with 34

[11, 12, 25, 34, 22, 64, 90]
...
```

**Code Structure**:
```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
```

**Advantages**:
- Simple to understand
- In-place sorting (O(1) space)
- Fewer swaps than bubble sort
- Good for small arrays

**Disadvantages**:
- O(n²) time complexity (always)
- Not adaptive
- Unstable (may change relative order)
- Slow for large arrays

## Performance Comparison

| Array Size | Bubble Sort | Selection Sort |
|------------|-------------|----------------|
| 10 elements | ~100 ops | ~45 ops |
| 100 elements | ~10,000 ops | ~4,950 ops |
| 1,000 elements | ~1,000,000 ops | ~499,500 ops |

**Note**: These are educational algorithms. For production, use built-in `sorted()` or more efficient algorithms like Quick Sort or Merge Sort.

## When to Use Which?

### Use Bubble Sort When:
- Array is very small (< 20 elements)
- Educational/learning purposes
- Need stable sort
- Simplicity is more important than speed

### Use Selection Sort When:
- Array is small (< 50 elements)
- Want to minimize swaps
- Educational/learning purposes
- Memory is very limited

### Use Built-in `sorted()` When:
- Array is large (> 100 elements)
- Production code
- Need optimal performance
- Don't need to understand internals

## Code Examples

### Example 1: Sorting Numbers

```python
numbers = [64, 34, 25, 12, 22, 11, 90]

# Bubble Sort
sorted_bubble = bubble_sort(numbers.copy())

# Selection Sort
sorted_selection = selection_sort(numbers.copy())

# Built-in (recommended for production)
sorted_builtin = sorted(numbers)
```

### Example 2: Sorting Strings

```python
words = ["banana", "apple", "cherry", "date"]

# Both algorithms work on strings
sorted_words = bubble_sort(words.copy())
```

### Example 3: Sorting in Descending Order

Modify the comparison:
```python
# Change > to < for descending order
if arr[j] < arr[j+1]:  # For bubble sort
```

## Learning Points

These implementations teach:
- **Algorithm Design**: Step-by-step problem solving
- **Time Complexity**: Understanding O(n²) complexity
- **Space Complexity**: In-place sorting concepts
- **Stability**: Maintaining relative order
- **Optimization**: When to use which algorithm

## Comparison with Other Algorithms

| Algorithm | Best Case | Average | Worst Case | Space | Stable |
|-----------|-----------|---------|------------|-------|--------|
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) | Yes |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) | No |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) | Yes |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) | No |
| Python sorted() | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes |

## Exercises

Try these exercises to practice:

1. **Count Comparisons**: Add counter to track number of comparisons
2. **Count Swaps**: Track number of swaps made
3. **Visualization**: Add print statements to show each step
4. **Reverse Sort**: Modify to sort in descending order
5. **Optimized Bubble Sort**: Add early termination if no swaps
6. **Insertion Sort**: Implement another O(n²) algorithm
7. **Compare Performance**: Time both algorithms on same data

## Further Reading

- [Sorting Algorithms](https://en.wikipedia.org/wiki/Sorting_algorithm)
- [Big O Notation](https://en.wikipedia.org/wiki/Big_O_notation)
- [Stable Sort](https://en.wikipedia.org/wiki/Sorting_algorithm#Stability)

## License

This project is open source and available for educational purposes.

---

**Master the art of sorting! 📊**
