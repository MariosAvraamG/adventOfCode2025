# Advent of Code 2015 - Day 5: Cafeteria Ingredient Management

## Problem Summary

The Elves in the cafeteria are struggling with a complex new **inventory management system** for their ingredients. The system provides two lists: a set of **fresh ingredient ID ranges** and a list of **available ingredient IDs**. The goal is to determine which ingredients are fresh based on these ranges.

* **Ingredient IDs:** Integers used to identify ingredients.
* **Fresh Ranges:** Inclusive ranges (e.g., `3-5` includes 3, 4, and 5).
* **Fresh Condition:** An ingredient ID is fresh if it falls within **any** of the fresh ranges.

---

## 🌟 Part One: Counting Available Fresh Ingredients

### Logic

The task is to find how many of the **available ingredient IDs** are considered fresh. Once an available ingredient is counted as fresh, it is **consumed** and should not be checked against subsequent ranges.

1.  Read and parse the input into a list of **Fresh Ranges (strings)** and a list of **Available Ingredients (strings/integers)**.
2.  Iterate through each **Fresh Range** (`L-U`).
3.  For that range, check the current list of available ingredients.
4.  If an ingredient ID $I$ is within the range ($\mathbf{L \le I \le U}$), increment the `fresh` count and **remove** the ingredient ID from the list of available ingredients.

**Final function used:** `get_fresh_ingredients`

### Result

| Part | Answer |
| :--- | :--- |
| Part One | **640** |

---

## 🌟🌟 Part Two: Total Count of Fresh IDs

### Logic

The goal changes: we need to find the **total number of unique ingredient IDs** that the **fresh ingredient ID ranges** define as fresh, ignoring the available ingredients list entirely. Since ranges can overlap (e.g., `10-14` and `12-18`), the overlaps must be counted only once.

### Approach (Interval Merging)

The most efficient solution avoids iterating over every single ID and instead relies on merging the range boundaries. 

1.  **Parse and Sort:** Convert all ranges to `(L, U)` integer tuples and sort them by the lower bound $L$.
2.  **Merge Overlaps:** Iterate through the sorted ranges, maintaining a `finalisedRanges` list.
    * If the current range overlaps with the last range in the `finalisedRanges` list, merge them by extending the upper bound of the last range: $\mathbf{U_{new} = \max(U_{prev}, U_{current})}$.
    * Otherwise, append the current range to the `finalisedRanges` list.
3.  **Calculate Count:** Sum the lengths of all non-overlapping ranges in `finalisedRanges`. Since the ranges are inclusive, the count for a range $(L, U)$ is $\mathbf{U - L + 1}$.

**Final function used:** `get_fresh_ingredient_ranges`

### Result

| Part | Answer |
| :--- | :--- |
| Part Two | **365804144481581** |