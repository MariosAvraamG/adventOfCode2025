def get_power_banks(filename):
    with open(filename, 'r') as f:
        return [powerBank.strip() for powerBank in f]

def choose_biggest_joltage(powerBanks):
    sumOfJoltage = 0
    resultLength = 12

    for powerBank in powerBanks:
        bankLength = len(powerBank)
        subs = bankLength-resultLength
        choices = []
        for digit in powerBank:
            joltage = int(digit)

            while(subs>0 and choices and joltage > choices[-1]):
                choices.pop()
                subs-=1
            
            choices.append(joltage)
        
        maxJoltageString = "".join(map(str, choices[:resultLength]))
        sumOfJoltage+=int(maxJoltageString)
    
    return sumOfJoltage

       


def main():
    powerBanks = get_power_banks('day 3/power_banks.txt')
    print(choose_biggest_joltage(powerBanks))

if __name__ == '__main__':
    main()