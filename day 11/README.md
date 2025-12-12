# 🔗 Advent of Code 2015 - Day 11: Reactor Conduits

## Problem Summary

This puzzle involves finding the number of distinct, unidirectional paths through a network of factory devices (conduits) modeled as a **Directed Acyclic Graph (DAG)**. We are asked to count paths between specific start and end nodes, first without constraints, and then with the constraint of visiting two mandatory intermediate nodes.

---

## 🌟 Part One: Simple Path Counting (you $\to$ out)

### Objective
Find the total number of unique paths from the starting device (`you`) to the main reactor output (`out`). Data flow is strictly unidirectional (forward through device outputs).

### Mathematical Formulation
This is a standard problem of counting paths in a DAG. Let $N(d \to \text{out})$ be the number of paths from device $d$ to $\text{out}$. The solution relies on the principle of **Dynamic Programming (DP)**:

$$
N(d \to \text{out}) = \sum_{d' \in \text{outputs}(d)} N(d' \to \text{out})
$$


### Logic & Implementation (`get_number_of_paths_memo`)
To ensure efficiency and handle large, merging path networks, the solution employs **Recursion with Memoization**:

1.  **Memoization Cache (`memo`):** A dictionary stores the path count for every device, preventing redundant calculations.
2.  **Base Cases:**
    * $N(\text{out} \to \text{out}) = 1$ (The path of length zero).
    * If a device has no path to $\text{out}$, $N(\dots) = 0$.
3.  **Recursive Step:** For any device, the total path count is the sum of the path counts of all its immediate output neighbors. The result is stored in the cache before returning.

This method transforms an exponential brute-force search into an efficient linear-time graph traversal ($O(V+E)$).

### Result
| Part | Answer |
| :--- | :--- |
| Part One | **753** |

---

## 🌟🌟 Part Two: Constrained Path Counting (svr $\to$ dac & fft $\to$ out)

### Objective
Find the total number of unique paths from the server rack (`svr`) to the output (`out`) that *must* visit both the digital-to-analog converter (`dac`) and the fast Fourier transform device (`fft`) in any order.

### Combinatorial Decomposition
Since the graph is unidirectional (a DAG), a path cannot flow backward. This allows us to break the complex constraint into two mutually exclusive and exhaustive path structures:

1.  **Structure 1 (dac $\to$ fft):** $\text{svr} \to \dots \to \text{dac} \to \dots \to \text{fft} \to \dots \to \text{out}$
2.  **Structure 2 (fft $\to$ dac):** $\text{svr} \to \dots \to \text{fft} \to \dots \to \text{dac} \to \dots \to \text{out}$

The total count is the sum of the counts for these two structures. 

### Mathematical Formulation
The problem is solved by multiplying the path counts of the independent segments for each structure:

$$\text{Total Paths} = (\mathbf{P}_{\text{svr} \to \text{dac}} \times \mathbf{P}_{\text{dac} \to \text{fft}} \times \mathbf{P}_{\text{fft} \to \text{out}}) + (\mathbf{P}_{\text{svr} \to \text{fft}} \times \mathbf{P}_{\text{fft} \to \text{dac}} \times \mathbf{P}_{\text{dac} \to \text{out}})$$

### Logic & Implementation (`get_number_of_special_paths`)
The generalized `get_number_of_paths_memo(start, end, memo, blocking)` function is reused, where:

* **`blocking` Parameter:** This critical parameter is used to correctly calculate segments like $\mathbf{P}_{\text{svr} \to \text{dac}}$. By setting `blocking='fft'`, we ensure the path does not prematurely visit the second mandatory node (`fft`) before reaching the first (`dac`), thus guaranteeing the paths used for the segments are mutually exclusive.

The function is called six times to calculate the necessary segments, and the results are combined using the formula above.

### Result
| Part | Answer |
| :--- | :--- |
| Part Two | **450854305019580** |