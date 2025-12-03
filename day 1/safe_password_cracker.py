def load_instructions(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f]

def extract_code(instructions):
    code = 0
    currentPos = 50

    for instruction in instructions:
        direction = instruction[0]
        movement = int(instruction[1:])
        if direction == "R":
            for _ in range(movement):
                currentPos = (currentPos + 1) % 100
                if currentPos == 0:
                    code += 1
        else:
            for _ in range(movement):
                currentPos = (currentPos - 1) % 100
                if currentPos == 0:
                    code += 1
    return code

def main():
    instructions = load_instructions('day 1/safe_instructions.txt')
    code = extract_code(instructions)
    print(code)

if __name__ == '__main__':
    main()