# Learn Data Structures by Building the Merge Sort Algorithm

## Project Overview

In this project, you will learn data structures and the divide-and-conquer approach by building the Merge Sort algorithm. Merge Sort is a sorting algorithm that divides a collection of data into smaller sub-parts, sorts them independently, and then merges the sorted sub-parts into a final sorted list.

This project helps you understand:

* Recursive problem-solving
* List slicing in Python
* Merging two sorted lists
* Index management in arrays

## How Merge Sort Works

1. **Divide**: The list is divided into two halves.
2. **Conquer**: Each half is recursively sorted.
3. **Merge**: The sorted halves are merged to produce a fully sorted list.

The recursion continues until sublists of length 1 are reached (already sorted), and then the merge step combines them back together in order.

## Code Example

```python
def merge_sort(array):
    if len(array) <= 1:
        return
    
    middle_point = len(array) // 2
    left_part = array[:middle_point]
    right_part = array[middle_point:]

    merge_sort(left_part)
    merge_sort(right_part)

    left_array_index = 0
    right_array_index = 0
    sorted_index = 0

    while left_array_index < len(left_part) and right_array_index < len(right_part):
        if left_part[left_array_index] < right_part[right_array_index]:
            array[sorted_index] = left_part[left_array_index]
            left_array_index += 1
        else:
            array[sorted_index] = right_part[right_array_index]
            right_array_index += 1
        sorted_index += 1

    while left_array_index < len(left_part):
        array[sorted_index] = left_part[left_array_index]
        left_array_index += 1
        sorted_index += 1
    
    while right_array_index < len(right_part):
        array[sorted_index] = right_part[right_array_index]
        right_array_index += 1
        sorted_index += 1


if __name__ == '__main__':
    numbers = [4, 10, 6, 14, 2, 1, 8, 5]
    print('Unsorted array: ')
    print(numbers)
    merge_sort(numbers)
    print('Sorted array: ' + str(numbers))
```

## Key Concepts Learned

* Recursion in Python
* Index management while merging lists
* Divide and Conquer algorithm design
* Python list slicing and iteration

