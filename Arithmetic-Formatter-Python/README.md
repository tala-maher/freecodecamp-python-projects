# 🧮 Arithmetic Formatter

A clean and educational Python project that takes a list of arithmetic problems and arranges them **vertically** and **side-by-side**, just like how they're written on paper in school.  
Ideal for learning string manipulation, condition checking, and clean formatting in Python.

---

## ✨ What This Project Does

✔️ Takes up to **five arithmetic problems** (addition and subtraction only).  
✔️ Checks for proper formatting and input validity.  
✔️ Aligns numbers and operators vertically for easy readability.  
✔️ Can **optionally display the answers**.  
✔️ Gives clear and meaningful **error messages** for invalid input.  

---

## 📌 Example Usage

```python
from arithmetic_formatter import arithmetic_arranger

print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))

## Output
   32      3801      45      123
+ 698    -    2    + 43    +  49
-----    ------    ----    -----
