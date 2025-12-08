# Advent of Code 2015 - Day 7: Laboratories

## Problem Summary

After exiting the trash compactor, we find ourselves in the "Teleporter Hub." Stepping onto the yellow teleporter pad, we are transported to a room with no doors. To escape, we must diagnose and repair the leaking **Tachyon Manifold**. Using error code `0H-N0`, we analyze a diagram where beams propagate through splitters.

* **S:** The tachyon beam entry point.
* **Splitter (^):** Stops the incoming beam and creates two new beams: one to the immediate left and one to the immediate right.
* **Empty Space (.):** Beams pass freely downward.

---

## 🌟 Part One: Manifold Beam Coverage

### Rule Set (Part One)

In the standard manifold, multiple beams can occupy the same space and merge. We are tasked with counting how many times a beam hits a splitter.

1.  **Merging:** If beams move into the same column, they merge into one.
2.  **Tracking:** The system only tracks whether a coordinate has *at least one* beam present.

### Logic

The function `get_path_splits` handles this by simulating the flow row by row using a **set**.

* **Grid Iteration:** Starting from `sourceIndex`, we track unique column indices in `flowingDirections`.
* **The Set Advantage:** Using a `set` automatically handles the merging properties; if two beams land on index `x`, the set retains only one entry for that column.
* **Split Counting:** Every time a column present in `flowingDirections` hits a `^` on the next row, the `splits` counter is incremented.

### Result

| Part | Answer |
| :--- | :--- |
| Part One | **1698** |

---

## 🌟🌟 Part Two: Quantum Many-Worlds Timelines

### Rule Set (Part Two)

The manifold is revealed to be **quantum**, following the "Many-Worlds" interpretation. A single particle is sent through, but every time it reaches a splitter, time itself bifurcates. Beams do **not** merge; overlapping paths represent distinct quantum histories.

1.  **Many-Worlds:** Every split doubles the existence of the particle arriving at that point.
2.  **History Tracking:** Even if paths cross, we must treat each journey as a unique timeline.

### Approach (Dynamic Programming)

The function `get_timelines` uses a `defaultdict(int)` to track the weight (number of timelines) at each column.

* **Weighted Propagation:** Instead of checking for existence, we look at the value `times` (the count of timelines reaching the current row/column).
* **Bifurcation:** If a splitter is hit, the current count of timelines (`times`) is added to both `direction + 1` and `direction - 1` for the subsequent row.
* **Final Count:** After iterating through the entire manifold grid, the total number of timelines is the sum of all values in the final `flowingDirections` dictionary.

### Result

| Part | Answer |
| :--- | :--- |
| Part Two | **95408386769474** |