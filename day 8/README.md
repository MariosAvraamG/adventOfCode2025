# Advent of Code 2015 - Day 8: Playground

## Problem Summary

After repairing the teleporter hub, we rematerialize in a massive underground space: a giant playground! A group of Elves are rigging an ambitious Christmas decoration project using small **electrical junction boxes** suspended in 3D space. 

While most boxes are inert, electricity flows between any two connected by a string of lights. To conserve materials, the Elves want to connect these boxes using the shortest straight-line distances possible to form a unified circuit that reaches every box.

---

## 🌟 Part One: Partial Circuitry

### Objective
Calculate the straight-line (Euclidean) distance between all possible pairs of junction boxes. Sort these by distance and connect the **1000 shortest pairs**. After these connections, find the sizes of the three largest resulting circuits and multiply them together.

### Logic & Implementation
* **Euclidean Distance:** I calculate the distance between any two junctions $J1(x1, y1, z1)$ and $J2(x2, y2, z2)$ using the 3D distance formula:
    $$d = \sqrt{(x2 - x1)^2 + (y2 - y1)^2 + (z2 - z1)^2}$$
* **Edge Sorting:** Every possible pair is generated and sorted globally, ensuring I always prioritize the shortest available connection.
* **Union-Find (DSU):** I use a **Disjoint Set Union** structure to manage the circuits. As we connect two boxes, their respective "sets" merge. This structure allows us to efficiently track the growth of circuit sizes and ignore redundant connections.



### Result
| Part | Answer |
| :--- | :--- |
| Part One | **83520** |

---

## 🌟🌟 Part Two: Full Connectivity

### Objective
Continue connecting the closest unconnected junction boxes until **every single box** in the input belongs to one large, unified circuit. Identify the **last** connection that bridges the final two remaining circuits and multiply the X coordinates of those two junction boxes.

### Logic
* **Connectivity Tracking:** We track the number of independent components (circuits). We start with $N$ individual circuits (one per box) and decrement this counter every time a connection successfully merges two distinct sets.
* **The "Final Bridge":** The moment the counter reaches `1`, we have identified the crucial final connection that joins the entire playground.
* **X-Coordinate Multiplication:** By capturing the indices $u$ and $v$ of this final edge, we retrieve their original X-coordinates from the input list and calculate the product.


### Result
| Part | Answer |
| :--- | :--- |
| Part Two | **1131823407** |

---