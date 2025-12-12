def get_connections(filename):
    connections = {}
    with open(filename, 'r') as f:
        for line in f:
            connections[line[0:3]] = line[4:].strip().split(' ')
    return connections

def get_number_of_paths_memo(device, connections, memo, destination, blocking):
    if device in memo:
        return memo[device]
    elif device == destination:
        return 1
    elif device == blocking:
        return 0
    
    count = 0
    for nextDevice in connections[device]:
        if destination == 'out':
            count += get_number_of_paths_memo(nextDevice, connections, memo, destination, blocking)
        elif nextDevice != 'out':
            count += get_number_of_paths_memo(nextDevice, connections, memo, destination, blocking)

    memo[device] = count
    return count

def get_number_of_special_paths(connections):
    dacPaths = get_number_of_paths_memo('svr', connections, {}, 'dac', 'fft')
    fftPaths = get_number_of_paths_memo('svr', connections, {}, 'fft', 'dac')
    dacToFft = get_number_of_paths_memo('dac', connections, {}, 'fft', '')
    fftToDac = get_number_of_paths_memo('fft', connections, {}, 'dac', '')
    dacToOut = get_number_of_paths_memo('dac', connections, {}, 'out', '')
    fftToOut = get_number_of_paths_memo('fft', connections, {}, 'out', '')
    paths = dacPaths*dacToFft*fftToOut + fftPaths*fftToDac*dacToOut
    return paths

def main():
    connections = get_connections('day 11/connections.txt')
    print(get_number_of_paths_memo('you', connections, {}, 'out', ''))
    print(get_number_of_special_paths(connections))

if __name__ == '__main__':
    main()