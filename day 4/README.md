# Advent of Code 2025 - Day 4: Printing Department Paper Rolls

## Problem Summary

The goal is to help the Elves by optimizing forklift routes in the Printing Department. We are given a grid representing rolls of paper (`@`) and empty floor space (`.`). Forklifts can only access a roll if the surrounding area isn't too crowded.

* Input: A grid map of paper rolls and empty space.
* Condition: A paper roll is **accessible** if it has **fewer than four** other paper rolls in its eight adjacent positions (Moore neighborhood).

---

## 🌟 Part One: Initial Accessible Rolls

### Logic

We must find the total count of paper rolls that are accessible *in the initial configuration* of the grid.

1. Iterate over every cell $(r, c)$ in the grid.
2. If the cell contains a paper roll (`@`):
    a. Count the number of `@` symbols in its 8 surrounding neighbors.
    b. If the count is $\text{count} < 4$, the roll is accessible.
3. Sum the count of all accessible rolls.

### Approach (Grid Iteration and Neighbor Counting)

The approach involves two nested loops to traverse the grid, and an inner loop to check the 8 neighbor positions for each paper roll. Boundary checks are essential to ensure indices don't go out of bounds.

### Result

| Part | Answer |
| :--- | :--- |
| Part One | **1560** |

---

## 🌟🌟 Part Two: Cascade Removal

### Logic

Once an accessible roll is removed (changing `@` to `.`), the accessibility of its neighbors might change, potentially allowing more rolls to be removed in the next step. This creates a chain reaction.

The goal is to find the **total number of rolls** that can be removed through this iterative process until no more rolls are accessible in the entire grid.

### Approach (Iterative Simulation)

This requires a simulation that repeats the Part One check until the grid stabilizes (no more rolls are accessible).

1.  **Initialize Grid:** List of strings as read from file
2.  **Simulation Loop:**
    a.  **Find Accessible:** Use the Part One logic to find the coordinates of all accessible rolls in the current grid state.
    b.  **Check Stop Condition:** If the list of accessible rolls is empty, stop the simulation.
    c.  **Remove Rolls:** Update the total removed count, and for every accessible roll found, change its character in the mutable grid from `@` to `.`.
    d.  **Repeat:** Go back to step 2a to re-evaluate the neighbors in the newly updated grid.

3.  The final result is the running total of removed rolls.

### Result

| Part | Answer |
| :--- | :--- |
| Part Two | **9609** |