'''
    Chapter 7 Exercises
'''
'''
    Graphs
'''
graphA = {
    'start':{'a':5,'b':2},
    'a':{'c':4,'d':2},
    'b':{'a':8,'d':7},
    'c':{'d':6,'finish':3},
    'd':{'finish':1},
    'finish':{}
}
graphB = {
    'start':{'a':10},
    'a':{'b':20},
    'b':{'c':1, 'finish':30},
    'c':{'a':1},
    'finish':{}
}
graphC = {
    'start':{'a':2, 'b':2},
    'a':{'c':2, 'finish':2},
    'b':{'a':2},
    'c':{'b':-1, 'finish':2},
    'finish':{}
}
'''
    Costs Tables
'''
infinity = float('inf')

costsA = {
    'a':5,
    'b':2,
    'c':infinity,
    'd':infinity,
    'finish':infinity
}
costsB = {
    'a':10,
    'b':infinity,
    'c':infinity,
    'finish':infinity
}
costsC = {
    'a':2,
    'b':2,
    'c':infinity,
    'finish':infinity
}
'''
    Parents Tables
'''
parentsA = {
    'a':'start',
    'b':'start',
    'c':None,
    'd':None,
    'finish':None
}
parentsB = {
    'a':'start',
    'b':None,
    'c':None,
    'finish':None
}
parentsC = {
    'a':'start',
    'b':'start',
    'c':None,
    'finish':None
}

'''
    The Dijktra's algorithm
'''
def Dijktra(graph,costs,parents):
    def find_lowest_cost_node(costs):
        lowest_cost = float('inf')
        lowest_cost_node = None
        for node in costs:
            cost = costs[node]
            if cost < lowest_cost and node not in processed:
                lowest_cost = cost
                lowest_cost_node = node
        return lowest_cost_node

    processed = []
    node = find_lowest_cost_node(costs)
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowest_cost_node(costs)
    return parents


print('Optimized route => {0}'.format(Dijktra(graphA,costsA,parentsA)))

print('Optimized route => {0}'.format(Dijktra(graphB,costsB,parentsB)))

print('Optimized route => {0}'.format(Dijktra(graphC,costsC,parentsC)))

