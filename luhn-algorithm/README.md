# luhn-algorithm-python

This project demonstrates how to work with numbers and strings in Python by implementing the **Luhn Algorithm**, which is widely used for validating identification numbers like **credit cards**.

## 📌 What is the Luhn Algorithm?

The **Luhn Algorithm** is a simple checksum formula used to validate a variety of identification numbers. It helps detect errors such as mistyped digits and is commonly used in:

- Credit card number verification
- IMEI numbers (for phones)
- National identification numbers

## ✅ Features

- Removes spaces and dashes from input
- Reverses digits as required
- Doubles every second digit from the right
- Sums digits properly (e.g., 12 → 1 + 2 = 3)
- Checks if the final sum is divisible by 10

