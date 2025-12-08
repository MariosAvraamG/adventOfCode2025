import math

def get_junctions(filename):
    with open(filename, 'r') as f:
        return [list(map(int, line.strip().split(','))) for line in f if line.strip()]

def get_sorted_edges(junctions):
    edges = []
    for i in range(len(junctions)):
        for j in range(i + 1, len(junctions)):
            p1, p2 = junctions[i], junctions[j]
            dist = math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 + (p1[2]-p2[2])**2)
            edges.append([dist, i, j])
    edges.sort()
    return edges

def solve_circuits(junctions, connections=1000):
    junctionsLen = len(junctions)
    edges = get_sorted_edges(junctions)
    
    parent = list(range(junctionsLen))
    circuit_size = [1] * junctionsLen

    def find(i):
        if parent[i] == i:
            return i
        return(find(parent[i]))

    def union(i, j):
        rooti, rootj = find(i), find(j)
        if rooti != rootj:

            if circuit_size[rooti] < circuit_size[rootj]:
                parent[rooti] = rootj
                circuit_size[rootj] += circuit_size[rooti]
            else:
                parent[rootj] = rooti
                circuit_size[rooti] += circuit_size[rootj]

    for edge in range(connections):
        _, u, v = edges[edge]
        union(u, v)

    final_sizes = [circuit_size[i] for i in range(junctionsLen) if parent[i] == i]
    final_sizes.sort(reverse=True)
    
    return final_sizes

def solve_all_connected(junctions):
    junctionsLen = len(junctions)
    edges = get_sorted_edges(junctions)
    
    parent = list(range(junctionsLen))
    remainingCircuits = junctionsLen

    def find(i):
        if parent[i] == i:
            return i
        return(find(parent[i]))

    for _, u, v in edges:
        rootu, rootv = find(u), find(v)

        if rootu != rootv:
            parent[rootu] = rootv
            remainingCircuits -= 1
            
            if remainingCircuits == 1:
                x1 = junctions[u][0]
                x2 = junctions[v][0]
                return x1 * x2
                
    return None #Will never reach this but done to avoid undefined behaviour

def main():
    junctions = get_junctions('day 8/junctions.txt')
    sizes = solve_circuits(junctions)
    result = sizes[0] * sizes[1] * sizes[2]
    print(result)
    print(solve_all_connected(junctions))

if __name__ == '__main__':
    main()