def get_rolls(filename):
    with open(filename, 'r') as f:
        return [rollLine.strip() for rollLine in f]
    
def find_accessible_rolls(rolls):
    accessibleRolls = []
    rollLength = len(rolls[0])
    for i in range(len(rolls)):
        for j in range(rollLength):

            if rolls[i][j] == '.':
                continue

            neighboringRolls = 0
            neighborDirections = [[-1, -1], [-1, 0], [-1, +1],  [0, -1], [0, +1], [+1, -1], [+1, 0], [+1, +1]]

            for direction in neighborDirections:
                iNeighbour = i+direction[0]
                jNeighbour = j+direction[1]

                if iNeighbour<0 or iNeighbour>=len(rolls) or jNeighbour<0 or jNeighbour>=rollLength:
                    continue
                else:
                    if rolls[iNeighbour][jNeighbour] == '@':
                        neighboringRolls+=1
                
            if neighboringRolls<4:
                accessibleRolls.append([i, j])
    
    return accessibleRolls


def remove_all_accessible_rolls(rolls):
    totalRollsRemoved = 0
    accessibleRolls = find_accessible_rolls(rolls)

    while len(accessibleRolls) > 0:
        totalRollsRemoved+=len(accessibleRolls)
        for accessibleRoll in accessibleRolls:
            newRollRow = rolls[accessibleRoll[0]][:accessibleRoll[1]] + '.' + rolls[accessibleRoll[0]][accessibleRoll[1]+1:] 
            rolls[accessibleRoll[0]] = newRollRow
        
        accessibleRolls = find_accessible_rolls(rolls)
    
    return totalRollsRemoved



def main():
    rolls = get_rolls('day 4/rolls.txt')
    print(remove_all_accessible_rolls(rolls))

if __name__ == '__main__':
    main()