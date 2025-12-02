# Advent of Code 2025 - Day 1

## Problem Summary
The Elves have a dial-based safe with numbers `0-99`.  
- The dial starts at `50`.  
- Rotations are given as `L` (left) or `R` (right) followed by a number of clicks.  
- The dial wraps around (0 after 99, 99 before 0).  

**Part One:** Count how many times the dial ends at 0 after each rotation.  
**Part Two:** Count how many times the dial points at 0 at any time, including during rotations.

---

## Approach
- Read rotations from `safe_instructions.txt`.  
- Track the dial position (`pos = 50` initially).  
- **Part One:** Update the position per rotation and count zeros at the end.  
- **Part Two:** Simulate each click and count every zero passed.  

---

## Results

| Part | Password |
|------|----------|
| Part One | 1018 |
| Part Two | 5815 |
