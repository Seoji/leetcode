# Runtime: 38ms
# Memory: 16.62MB

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        def bfs(start, end):
            if start not in graph or end not in graph:
                return -1
            elif start == end:
                return 1

            queue = deque([(start, 1)])
            visited = set()
            visited.add(start)
            while queue:
                node, val = queue.popleft()
                for nextNode, w in graph[node]:
                    if nextNode == end:
                        return val * w

                    if nextNode not in visited:
                        queue.append((nextNode, val * w))
                        visited.add(nextNode)

            return -1

        graph = defaultdict(list)
        for (a, b), value in zip(equations, values):
            graph[a].append((b, value))
            graph[b].append((a, 1 / value))

        return [bfs(*query) for query in queries]
