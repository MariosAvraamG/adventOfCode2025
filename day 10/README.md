# 🎄 Advent of Code 2015 - Day 10: Factory Initialization

## Problem Summary

This puzzle involves initializing factory machines by meeting two distinct configuration challenges: first, toggling indicator lights to match a diagram, and second, setting joltage counters to specific required levels. Both challenges involve finding the minimum number of button presses, making them problems of constrained optimization.

---

## 🌟 Part One: Indicator Lights (XOR Logic)

### Objective
Find the minimum total button presses required to configure all indicator lights on a machine to match a target pattern (`.`=off/0, `#`=on/1). Each button press toggles (XORs) the state of the affected lights.

### Mathematical Formulation
This problem is a classic application of Linear Algebra over the **Finite Field $\mathbb{F}_2$ (GF(2))**.
$$
\mathbf{A}\mathbf{x} = \mathbf{b} \pmod{2}
$$
* **$\mathbf{A}$ (Matrix):** The columns represent the buttons. $A_{ij} = 1$ if button $j$ affects light $i$, and $0$ otherwise.
* **$\mathbf{b}$ (Vector):** The target state of the lights (1 for `#`, 0 for `.`).
* **$\mathbf{x}$ (Solution Vector):** The number of times each button is pressed. Since $x_i \pmod 2$ is what matters, $x_i \in \{0, 1\}$.

### Logic & Implementation (`find_local_min`)
Since the press count $x_i$ can only be 0 or 1 modulo 2, the total search space is $2^N$, where $N$ is the number of buttons. Given $N$ is small, a brute-force approach is feasible:

1.  **Search Space:** Iterate through all $2^N$ combinations of button presses (`itertools.product([0, 1], ...)`).
2.  **Toggle Simulation:** For each combination $\mathbf{x}$, simulate the toggling action using the XOR operator (`^`) to check if the final `result` equals the target $\mathbf{b}$.
3.  **Minimization:** Find the solution $\mathbf{x}$ that satisfies the equation and minimizes the sum of its components ($\sum x_i$).

### Result
| Part | Answer |
| :--- | :--- |
| Part One | **532** |

---

## 🌟🌟 Part Two: Joltage Requirements (Integer Linear Programming)

### Objective
Find the minimum total button presses required to increase the joltage counters (starting at 0) to exactly match the target requirements. Each press adds 1 to the affected counters.

### Mathematical Formulation
This is a constrained optimization problem known as **Integer Linear Programming (ILP)**.
$$
\min \sum_{i} x_i \quad \text{subject to:}
$$
1.  **Equality:** $\mathbf{A}\mathbf{x} = \mathbf{b}$
2.  **Non-Negativity:** $\mathbf{x} \ge \mathbf{0}$
3.  **Integrality:** $\mathbf{x} \in \mathbb{Z}^N$ (Presses must be integers)

* **$\mathbf{A}$ (Matrix):** Identical to Part One. $A_{ij} = 1$ if button $j$ affects counter $i$.
* **$\mathbf{b}$ (Vector):** The target joltage requirements.
* **$\mathbf{x}$ (Solution Vector):** The number of times each button is pressed.

### Logic & Implementation (`solve_machine_ilp`)
Solving ILP problems requires dedicated high-performance algorithms. Instead of a slow brute-force search over the null space, the solution leverages the `scipy.optimize.milp` function with the efficient **HiGHS** solver:

1.  **Objective (`c`):** Defined as `np.ones(num_buttons)` to minimize the sum $\sum x_i$.
2.  **Constraints:**
    * **Equality:** Handled by `LinearConstraint(A, target, target)`.
    * **Non-Negativity:** Handled by `Bounds(lb=0, ub=np.inf)`.
    * **Integrality:** Handled by `integrality = np.ones(num_buttons)`.
3.  **Solver Execution:** The `milp` function finds the provably optimal integer solution.

This approach is highly robust and avoids the computational pitfalls of custom Null Space searching.

### Result
| Part | Answer |
| :--- | :--- |
| Part Two | **18387** |