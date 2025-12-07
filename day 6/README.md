# Advent of Code 2015 - Day 6: Trash Compactor (Cephalopod Math)

## Problem Summary

While taking an over-enthusiastic trip down the garbage chute, we find ourselves in a magnetically sealed garbage smasher. We agree to help a family of cephalopods with their math homework to pass the time. The assignment is a single, large worksheet containing many arithmetic problems (addition **(+)** or multiplication **(\*)**) arranged horizontally in columns.

* **Problems:** Groups of numbers followed by a single operator symbol on the bottom line.
* **Separation:** Problems are separated by a full column of only spaces.
* **Goal:** Calculate the answer for every individual problem and return the **Grand Total** by summing all of the individual results.

---

## 🌟 Part One: Vertical Number Construction (Left-to-Right)

### Rule Set (Part One)

The initial, standard assumption for reading the problems is:

1.  **Reading Direction:** Problems are processed from **Right-to-Left**.
2.  **Number Construction:** Each number for a problem is found in a separate row. The numbers in a problem group are arranged **vertically**.
    * *Example:* The first problem block has numbers **8373**, **788**, **187** and **65**, all read horizontally from their respective rows. The operator is **+**.

### Logic

The implementation must correctly group the numbers based on the column boundaries defined by the separators (full column of spaces).

1.  **Grid Formation:** The multi-line text file input is treated as a grid to ensure consistent column indexing.
2.  **Number Extraction:** Iterate through the columns and extract the number found in each row. Because the numbers can be misaligned, the standard `split()` function is often insufficient. Instead, a column-based approach or a carefully managed `split()` is used to extract the numbers from each row.
3.  **Problem Grouping:** The numbers from all rows that fall between two separator columns form a single problem. The operator is read from the bottom line of the block.
4.  **Calculation:** The arithmetic is performed (addition or multiplication) and the result is accumulated into the **Grand Total**.

**Final function used:** `solve_maths_part1` combined with the grouping logic (`read_problems_part1`).

### Result

| Part | Answer |
| :--- | :--- |
| Part One | **4580995422905** |

---

## 🌟🌟 Part Two: Right-to-Left, Vertical Digits

### Rule Set (Part Two)

The true, complex cephalopod math rules change the entire interpretation:

1.  **Reading Direction:** Problems are processed from **Right-to-Left**.
2.  **Number Construction:** The digits of a single number are spread **vertically** across multiple rows. Each column (excluding separators) represents a single number, read top-to-bottom.
    * *Example:* The leftmost problem in the example is formed by columns, and the rightmost number is found by reading column by column from right-to-left. The final problem is **3 + 787 + 388 + 8716**.

### Approach (Transposition and Reverse Iteration)

The solution requires a fundamental shift in iteration and number construction to respect the new rules.

1.  **Grid Preparation:** Input rows to form a perfect character grid.
2.  **Right-to-Left Problem Identification:** The columns are iterated from the **rightmost** to the leftmost. Consecutive non-separator columns are collected into a problem block.
3.  **Number Extraction (Vertical Digits):** Within the problem block, each column itself forms a single number by concatenating its non-space characters from top-to-bottom.
4.  **Block Solving:** When a separator column is encountered, the collected block defines a single problem. The **numbers** for the problem are the vertically constructed numbers from each column in the block.
5.  **Calculation:** The appropriate operation is performed on these numbers, and the result is added to the **Grand Total**.

**Final function used:** `solve_math` and `read_problems`

### Result

| Part | Answer |
| :--- | :--- |
| Part Two | **10875057285868** |