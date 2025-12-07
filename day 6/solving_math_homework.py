def read_problems(filename):
    with open(filename, 'r') as f:
        mathOperations = []
        mathNumbers = []
        lines = f.readlines()
        nums = []
        for i in range(len(lines[-1])):
            if lines[-1][i] == '+' or lines[-1][i] == '*':
                mathOperations.append(lines[-1][i])
                if nums:
                    mathNumbers.append(nums)
                    nums = []
            num = ''
            if lines[0][i] != ' ':
                num+=lines[0][i]
            if lines[1][i] != ' ':
                num+=lines[1][i]
            if lines[2][i] != ' ':
                num+=lines[2][i]
            if lines[3][i] != ' ':
                num+=lines[3][i]
            if num != '':
                nums.append(int(num))
        
        mathNumbers.append(nums)


    return mathOperations, mathNumbers

def read_problems_part1(filename):
    with open(filename, 'r') as f:
        mathContents = []
        for line in f:
            mathContents.append([value.strip() for value in line.split(' ') if value.strip() != ''])
    return mathContents

def solve_maths_part1(problems):
    result = 0
    for i in range(len(problems[-1])):
        operation = problems[-1][i]

        if operation=='+':
            result+=(int(problems[0][i]) + int(problems[1][i]) + int(problems[2][i]) + int(problems[3][i]))
        else:
            result+=(int(problems[0][i]) * int(problems[1][i]) * int(problems[2][i]) * int(problems[3][i]))
    return result

def solve_maths(operations, numbers):
    result = 0
    for i in range(len(operations)):
        operation = operations[i]
        if operation == '+':
            result += sum(numbers[i])
        else:
            product = 1
            for num in numbers[i]:
                product =product* num
            result+= product
    return result

def main():
    operations, numbers = read_problems('day 6/math_problem.txt')
    print(solve_maths(operations, numbers))

if __name__ == '__main__':
    main()