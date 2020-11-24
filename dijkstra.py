# let's have string as the location and one dict as its neighbors
# the start point has the name 'start' and the end point has the name 'end'
# we have visited list to store the locations that we have visited
# we have parents dict to store the parent of each location such that the final path has the shortest distances
# Dijkstra Algorithm can solve problems that DON'T have negative weights
# the loop is not a big deal, cause one pass and detour can't give us better distance

def dijkstra(path):
    visited = []
    parents = {}
    cost = {}


    def init():
        for k, v in path['start'].items():
            cost[k] = v
            parents[k] = 'start'
        parents['start'] = None

    def find_the_min_cost_node():
        minimum = float('inf')
        target = None
        for k, v in cost.items():
            if k not in visited and v < minimum:
                target = k
                minimum = v
        return target, minimum

    def get_full_path():
        stack = []
        pointer = 'end'
        while pointer is not None:
            stack.append(pointer)
            pointer = parents[pointer]
        stack.reverse()
        return stack

    init()
    for _ in range(1, len(path)):
        current, dist = find_the_min_cost_node()
        if current is None:
            break
        else:
            for neighbor, distance in path[current].items():
                if neighbor not in cost.keys() or dist + distance < cost[neighbor]:
                    cost[neighbor] = dist + distance
                    parents[neighbor] = current
            visited.append(current)
    if 'end' in cost.keys():
        return get_full_path()
    else:
        print("there is no path")
        return None


graph = {"start": {"a": 6, "b": 2}, "a": {"end": 1}, "b": {"a": 3, "end": 5}, "end": {}}
route = dijkstra(graph)
print(route)
