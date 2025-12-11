import itertools
import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds

def read_schematic(filename):
    with open(filename, 'r') as f:
        lights = []
        buttons = []
        joltageRequirements = []
        for line in f:
            elements = line.strip().split(' ')
            currentButtons = []
            for element in elements:
                if element[0] == '[':
                    lights.append(element[1:-1])
                elif element[0] == '(':
                    currentButtons.append(list(map(int, element[1:-1].split(','))))
                else:
                    joltageRequirements.append(list(map(int, element[1:-1].split(','))))
            buttons.append(currentButtons)
        return lights, buttons, joltageRequirements



def find_local_min(light, buttons):
    b = [1 if char == '#' else 0 for char in light]
    A = []
    for button in buttons:
        col = [0] * len(light)
        for i in button:
            col[i] = 1
        A.append(col)

    minPresses = float('inf')

    for x in itertools.product([0, 1], repeat=len(buttons)):
        presses = sum(x) 
        
        result = [0] * len(light)
        
        for col in range(len(buttons)):
            if x[col] == 1:
                Acol= A[col]
                result = [result[i] ^ Acol[i] for i in range(len(light))]
                
        if result == b:
            minPresses = min(minPresses, presses)

    return minPresses
    
def find_min_moves(lights, buttons):
    minCount = 0
    for i in range(len(lights)):
        minCount += find_local_min(lights[i], buttons[i])
    return minCount


def solve_machine_ilp(joltage_req, buttons):

    target = np.array(joltage_req)
    num_buttons = len(buttons)
    num_counters = len(target)

    A = np.zeros((num_counters, num_buttons))
    for j, indices in enumerate(buttons):
        for i in indices:
            if i < num_counters:
                A[i, j] = 1

    c = np.ones(num_buttons)
    constraints = LinearConstraint(A, target, target)
    integrality = np.ones(num_buttons)
    bounds = Bounds(lb=0, ub=np.inf)
    res = milp(c=c, constraints=constraints, integrality=integrality, bounds=bounds)

    return res.x.sum()
        
def set_joltage(joltageRequirements, buttons):
    minCount = 0
    for i in range(len(joltageRequirements)):
        minCount += solve_machine_ilp(joltageRequirements[i], buttons[i])
    return minCount

def main():
    lights, buttons, joltageRequirements = read_schematic('day 10/wiring_schematic.txt')
    print(find_min_moves(lights, buttons))
    print(set_joltage(joltageRequirements, buttons))

if __name__ == '__main__':
    main()