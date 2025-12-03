def load_ids(filename):
    with open(filename, 'r') as f:
        return [values.strip() for values in f.readline().split(',')]

def get_invalid_sum(idRanges):
    invalidSum = 0
    for idRange in idRanges:
        bottomLimit, topLimit = map(int, idRange.split('-'))
        for value in range(bottomLimit, topLimit):
            valueStr = str(value)

            if valueStr in (valueStr + valueStr)[1:-1]:
                invalidSum += value

    return invalidSum

def main():
    idRanges = load_ids('day 2/password_ranges.txt')
    print(get_invalid_sum(idRanges))


if __name__ == '__main__':
    main()