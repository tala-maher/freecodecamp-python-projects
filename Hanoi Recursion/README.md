# Tower of Hanoi Recursion

This project is a Python implementation of the classic **Tower of Hanoi** puzzle. It focuses on learning **recursion**, a fundamental programming concept, by solving the problem step by step.

## Project Overview

The Tower of Hanoi puzzle consists of three rods and a number of disks of different sizes. The goal is to move all disks from the **source rod** to the **target rod**, following these rules:

1. Only one disk can be moved at a time.
2. Only the top disk of a rod can be moved.
3. A larger disk cannot be placed on top of a smaller disk.

## Learning Goals

By completing this project, you will:

* Understand the concept of **recursion** and how a function can call itself.
* Break down a complex problem into smaller sub-problems.
* Learn how to manipulate **lists** in Python.
* Visualize the step-by-step solution of the Tower of Hanoi puzzle.

## How the Code Works

1. Three lists represent the rods: `A` (source), `B` (auxiliary), and `C` (target).
2. The recursive function `move(n, source, auxiliary, target)` moves `n` disks from the source rod to the target rod using the auxiliary rod.
3. Base case: When `n == 0`, the recursion stops.
4. Recursive case:

   * Move `n-1` disks from `source` to `auxiliary` using `target`.
   * Move the largest disk from `source` to `target`.
   * Move the `n-1` disks from `auxiliary` to `target` using `source`.
5. After each move, the state of the rods is printed to visualize the puzzle's progression.


## Example Output

For 3 disks:

```
[3, 2, 1] [] []
[3, 2] [] [1]
[3] [2] [1]
[3] [2, 1] []
[] [2, 1] [3]
[1] [2] [3]
[1] [] [3, 2]
[] [] [3, 2, 1]
```
