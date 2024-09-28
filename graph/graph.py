from collections import defaultdict
from collections import deque


class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def reset(self):
        self.graph.clear()

    def print(self):
        print("-----  ----- ")
        for key, value in self.graph.items():
            print(key, " --> ", value)

    def addEdge(self, u, v, direction, weighted=False, weight=None):
        # direction : 0 == undirected
        # direction : 1 == directed
        if not weighted:
            self.graph[u].append(v)
            if direction == 0:
                self.graph[v].append(u)

        if weighted:
            self.graph[u].append((v, weight))
            if direction == 0:
                self.graph[v].append((u, weight))

    def build(self):
        # undirected 
        self.addEdge(0, 1, 0)
        self.addEdge(1, 2, 0)
        self.addEdge(0, 2, 0)

        self.print()
        # self.reset()

        bfs = self.bfs(self.graph, 0)
        print(bfs)

        # # directed
        # self.addEdge(0, 1, 1)
        # self.addEdge(1, 2, 1)
        # self.addEdge(0, 2, 1)
        #
        # self.print()
        # self.reset()
        #
        # # weighted
        # self.addEdge(0, 1, 1, weighted=True, weight=3)
        # self.addEdge(1, 2, 1, weighted=True, weight=5)
        # self.addEdge(0, 2, 1, weighted=True, weight=11)
        #
        # self.print()
        # self.reset()

    def bfs(self, graph, start):
        q = deque()
        visited = set()

        q.append(start)
        
        result = []
        while q:
            node = q.popleft()
            
            if node not in visited:
                result.append(node)
                visited.add(node)
                
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        q.append(neighbor)
        return result

    def dfs(self):
        pass