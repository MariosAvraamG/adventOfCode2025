# Advent of Code 2025 - Day 3: Battery Bank Overload

## Problem Summary

I was tasked with analyzing sequences of digits (representing battery joltages) within various "power banks." The goal is to calculate the total output joltage based on specific rules for selecting digits from each bank while maintaining their original order.

* Input: A list of battery banks, where each bank is a string of digits (e.g., ["987654321111111", "811111111111119"]).

* Constraint: Selected digits must maintain their original relative order from the bank.

## 🌟 Part One: Largest Two-Digit Joltage

### Logic

The joltage output for each bank is the largest possible two-digit number formed by selecting exactly two batteries (digits, d1 and d2) such that d1 appears before d2 in the bank.

The final result is the sum of these maximum two-digit joltages across all banks.

### Approach (Brute-Force Pair Iteration)

1. Initialize a total sum for the output joltage.

2. For each bank:
   a.  Initialize maxBankJoltage to 0.
   b.  Iterate through all possible positions for the first digit, d1 (index i).
   c.  For each d1, iterate through all subsequent positions for the second digit, d2 (index j > i).
   d.  Calculate the two-digit number: J = (d1 x 10) + d2.
   e.  Update maxBankJoltage = max(maxBankJoltage, J).

3. Add maxBankJoltage to the total sum.

### Result

| Part | Answer | 
|---|---|
| Part One | 17034 | 

## 🌟🌟 Part Two: Largest Twelve-Digit Joltage

### Logic

The escalator requires an extreme joltage limit override. Now, you must make the largest possible number by selecting exactly twelve batteries (digits) from each bank, again maintaining their original order.

The final result is the sum of these maximum twelve-digit joltages across all banks.

### Approach (Greedy Algorithm)


To maximize a number by removing a fixed number of digits (subs = bankLength - 12), we must ensure the most significant (leftmost) digits are as large as possible.

1. Calculate Removals: Determine the number of digits to remove: subs = bankLength - 12.

2. Initialize Stack: Use a list (choices) to store the selected digits; this list acts like a stack.

3. Greedy Iteration: Iterate through each digit representing a joltage in the bank:
   a.  Removal Check: While subs > 0, the choices list is not empty, and the current joltage is greater than the last joltage added (choices[-1]):
   * Remove the suboptimal joltage: choices.pop().
   * Decrement removals: subs -= 1.
   b.  Add the current joltage: choices.append(joltage).

4. Finalize: Trim the choices list to the required length: choices[:12].

5. Summation: Convert the resulting 12-digit sequence into a single large integer and add it to the total output joltage.

### Result

| Part | Answer | 
|---|---|
| Part Two | 168798209663590 |