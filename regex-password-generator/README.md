# Regex Password Generator

A secure and customizable **password generator** built in Python to practice and learn **Regular Expressions (Regex)**. This project demonstrates how to use Python's `secrets` module for secure random password generation and the `re` module to validate password constraints efficiently.

## Features

* Generate passwords of any length.
* Customize minimum number of:

  * Digits
  * Uppercase letters
  * Lowercase letters
  * Special characters
* Secure random selection using `secrets`.
* Validate password constraints using regex and Python's `all()` function.
* Efficient memory usage with generator expressions.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/regex-password-generator.git
cd regex-password-generator
```

2. Make sure Python 3 is installed.

## Usage

Import the `generate_password` function from the module and call it with your desired constraints:

```python
from password_generator import generate_password

# Generate a password with 8 characters and at least 1 of each constraint
new_password = generate_password(
    length=8,
    nums=1,
    special_chars=1,
    uppercase=1,
    lowercase=1
)

print(new_password)
```

## How It Works

* **Character Pools**: Combines letters, digits, and special characters.
* **Random Selection**: Uses Python's `secrets.choice()` for cryptographically secure random selection.
* **Validation**:

  * Uses `re.findall()` with regex patterns for each constraint.
  * Uses `all()` with generator expressions to ensure all constraints are met.
* **Regeneration**: If a generated password does not meet all constraints, it regenerates until it does.

## Example Output

```
Generated password: Ab3$gH7!
```

