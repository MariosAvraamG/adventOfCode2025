# Advent of Code 2015 - Day 9: Movie Theater

## Problem Summary

We've been tasked by the Elves to find the optimal seating for a film crew using a special type of tile in a large grid. The input provides an ordered list of **Red Tiles** that form the vertices of a large, closed, axis-aligned polygon.

---

## 🌟 Part One: Largest Rectangle (Unrestricted)

### Objective
Find the largest possible area of any axis-aligned rectangle whose opposite corners are occupied by any two **Red Tiles** from the input list.

### Logic & Implementation
* **Brute Force $O(N^2)$:** Since the number of Red Tiles ($N$) is manageable, we check every unique pair of Red Tiles $(x1, y1)$ and $(x2, y2)$ as potential opposite corners.
* **Area Calculation:** The area of a rectangle spanning these two tile coordinates (inclusive of the tiles themselves) is calculated using the formula:
    $$\text{Area} = (|x2 - x1| + 1) \times (|y2 - y1| + 1)$$
* **Edge Case:** Pairs that lie on the same row or column (resulting in a line or point, $\text{dx}=0$ or $\text{dy}=0$) are ignored as they do not form a proper rectangle.

### Result
| Part | Answer |
| :--- | :--- |
| Part One | **4749929916** |

---

## 🌟🌟 Part Two: Largest Rectangle (Constrained)

### Problem Constraint
The resulting rectangle is only valid if **every tile** it contains is either **Red** or **Green**. Green tiles are those on the segments connecting the Red Tiles *and* all tiles strictly inside the polygon formed by the Red Tiles. 

### Objective
Find the largest rectangle area that satisfies the constraint: using two Red Tiles as opposite corners, any other tile included in the rectangle must be Red or Green.

### Logic & Implementation
Given that the coordinate space is massive ($X_{\text{max}} \times Y_{\text{max}}$ is too large for memory), the solution must avoid generating the complete set of Red/Green tiles and must rely on geometric algorithms.

#### 1. Core Constraint Check ($O(N^3)$)
The largest bottleneck is checking the $O(N^2)$ pairs. For each candidate rectangle defined by $P1(x1, y1)$ and $P2(x2, y2)$, we must validate the two new corners: $C3(x1, y2)$ and $C4(x2, y1)$.

* **Validation 1 (Point-in-Polygon):** We use an $O(N)$ **Point-in-Polygon (PIP) check** (Ray Casting) to determine if $C3$ and $C4$ are inside or on the boundary of the polygon. This avoids the $O(X{\text{max}} \times Y{\text{max}})$ grid iteration. 

* **Validation 2 (Boundary Intersection):** Since the polygon is non-convex (it can be U-shaped), checking only the corners is insufficient. We must verify that no segment of the Red Tile boundary cuts through the interior of the candidate rectangle, which would indicate the rectangle is "bridging a gap" and enclosing invalid tiles.

#### 2. Intersection Check
A dedicated function checks if any segment defined by two adjacent Red Tiles intersects the **interior** of the candidate rectangle. If an intersection occurs, the rectangle is rejected.

The final result is the maximum area found among all rectangles that pass **both** the PIP check and the boundary intersection check.

### Result
| Part | Answer |
| :--- | :--- |
| Part Two | **1572047142** |