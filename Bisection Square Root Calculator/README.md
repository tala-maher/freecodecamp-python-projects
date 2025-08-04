# Square Root Estimator using Bisection Method

This is a Python project that estimates the square root of a number using the **bisection method**, a form of **binary search**. It approximates the result up to a user-defined tolerance.

## 📌 Features

- Works for any non-negative real number
- Customizable precision using a tolerance value
- Iterative approach (no recursion)
- Demonstrates the power of numerical approximation

## 🧮 How It Works

The algorithm:
1. Initializes a search interval `[low, high]`
2. Repeatedly narrows the interval by comparing the square of the midpoint with the target value
3. Stops when the square of the midpoint is close enough to the target (within the tolerance)

## 🐍 Technologies Used

- Python 3
- Built-in functions: `abs()`, `max()`, `range()`

## 🧠 Concepts Covered

- Binary search (bisection method)
- Floating-point arithmetic
- Absolute error and tolerance
- Efficient problem-solving without built-in `sqrt()`

