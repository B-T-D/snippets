from graph_from_txt import read_graph

def bfs(network, source):
    """Perform a breadth-first search on network, starting from source.

    Args:
        network (dict): a graph represented by a dict
        source: the node in network from which to start the BFS

    Returns:
        distance (dict): a dictionary with distances from source to each node.
        predecessor (dict): a dictionary listing the node preceding each node
            on the shortest path from it to the source.
    """
    distance = {}
    predecessor = {}
    for node in network:
        distance[node] = float('inf')
        predecessor[node] = None
    distance[source] = 0
    queue = [source]
    while queue != []:
        front = queue.pop(0)
        for neighbor in network[front]:
            if distance[neighbor] == float('inf'):
                distance[neighbor] = distance[front] + 1
                predecessor[neighbor] = front
                queue.append(neighbor)
    return distance, predecessor

def closeness_centrality(network, node):
    """
    Returns:
        (int): closeness centrality of node
    """
    distances = bfs(network, node)[0]
    total_distance = 0
    for dest in distances:
        if distances[dest] == float('inf'):
            dist[dest] = len(network) # if no paths set distance to number of nodes
        total_distance += distances[dest]
    return total_distance



filename = 'clusters.txt'
network = read_graph(filename)

colwidth_node = 20
colwidth_ccent = 25
print(f"{'Node':^{colwidth_node}}|{'Closeness centrality':^{colwidth_ccent}}")
print('-' * colwidth_node + '|' + '-' * colwidth_ccent)
for node in network:
    ccent = closeness_centrality(network, node)
    print(f"{node:^{colwidth_node}}|{ccent:^{colwidth_ccent}}")

