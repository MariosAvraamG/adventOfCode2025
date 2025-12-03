# Advent of Code 2025 - Day 2: Gift Shop

## Problem Summary
The North Pole gift shop database has been corrupted by a young Elf who added invalid Product IDs using repeating patterns. The goal is to scan specific ranges of IDs provided in the puzzle input and calculate the sum of all invalid IDs found.

- **Input:** A long string of comma-separated ID ranges (e.g., `11-22, 95-115`).
- **Constraint:** IDs are made only of digits and cannot have leading zeros.

***

## 🌟 Part One: Sequence Repeated Twice

### Logic
An ID is invalid if it is formed by a sequence of digits repeated **exactly twice** (e.g., `123123` or `55`).

### Approach
1.  **Parse** the input ranges.
2.  Iterate through every id (`value`) in each range.
3.  Convert `value` to a string.
4.  Check if `len(string)` is even.
5.  If even, check if the first half equals the second half: `s[:len(s)//2] == s[len(s)//2:]`.
6.  Sum all numbers that meet this condition.

### Result
| Part | Answer |
|------|----------|
| Part One | **28844599675** |

***

## 🌟🌟 Part Two: Sequence Repeated At Least Twice

### Logic
An ID is invalid if it is formed by a sequence of digits repeated **two or more times** (e.g., `123123`, `121212`, or `111`). This is a check for string **periodicity**.

### Approach
1.  The core iteration remains the same as Part One.
2.  The validation check is changed to determine if the string is a non-trivial rotation of itself.
3.  An efficient way to check this is to see if the string `s` is contained within the doubled string `s+s` after removing the first and last characters:
    * `if s in (s + s)[1:-1]:`
4.  Sum all numbers that meet this new periodic condition.

### Result
| Part | Answer |
|------|----------|
| Part Two | **48778605167** |