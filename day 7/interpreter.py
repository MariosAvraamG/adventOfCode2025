from collections import defaultdict

def read_manifold(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f.readlines()]

def find_source(manifold):
    for i in range(len(manifold[0])):
        if manifold[0][i] == 'S':
            return i

def get_path_splits(manifold):
    sourceIndex = find_source(manifold)
    flowingDirections = {sourceIndex}

    splits = 0
    for i in range(1, len(manifold)):
        newDirections = set()

        for direction in flowingDirections:
            if manifold[i][direction] == '^':
                splits+=1

                newDirections.add(direction+1)
                newDirections.add(direction-1)
                
            else:
                newDirections.add(direction)
        
        flowingDirections = newDirections

    return splits

def get_timelines(manifold):
    sourceIndex = find_source(manifold)
    flowingDirections = {sourceIndex: 1}

    for i in range(1, len(manifold)):
        timelines = defaultdict(int)
        for direction, times in flowingDirections.items():
            if manifold[i][direction] == '^':
                timelines[direction+1] += times
                timelines[direction-1] += times     
            else:
                timelines[direction]+=times
        
        flowingDirections = timelines

    return sum(flowingDirections.values())
    


def main():
    manifold = read_manifold('day 7/tachyon_manifold.txt')
    print(get_path_splits(manifold))
    print(get_timelines(manifold))


    
if __name__ == '__main__':
    main()