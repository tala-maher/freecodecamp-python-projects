# Merge Sort Algorithm

## Project Overview

This Python script implements the Merge Sort algorithm. Merge Sort is a sorting algorithm that:

* Divides a list of numbers into smaller sublists,
* Recursively sorts each sublist,
* Merges the sorted sublists to produce a fully sorted list.

## What the Code Does

* Takes an unsorted list of numbers.
* Recursively divides the list into two halves until each sublist has one element.
* Merges the sublists in sorted order.
* Prints the original unsorted list and the final sorted list.

## Example

```python
numbers = [4, 10, 6, 14, 2, 1, 8, 5]
print('Unsorted array:')
print(numbers)
merge_sort(numbers)
print('Sorted array: ' + str(numbers))
```


