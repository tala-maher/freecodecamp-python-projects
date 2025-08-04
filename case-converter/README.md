# 🐍 Case Converter: From CamelCase to snake_case

This mini project demonstrates how to convert a string written in `CamelCase` or `PascalCase` into `snake_case` using Python. The main purpose of this project is to practice **list comprehension**, **string manipulation**, and **method chaining**.

## 🚀 What You'll Learn

- How to iterate over strings in Python
- How to detect uppercase letters
- How to transform characters using list comprehensions
- How to chain string methods (`join`, `strip`)
- The difference between `if` filtering and `if/else` expressions inside list comprehensions

## 🧠 Code Logic

```python
pascal_or_camel_cased_string = "CamelCase"

snake_cased_char_list = [
    ('_' + char.lower()) if char.isupper() else char
    for char in pascal_or_camel_cased_string
]

snake_case_string = ''.join(snake_cased_char_list).strip('_')
print(snake_case_string)  # Output: camel_case
