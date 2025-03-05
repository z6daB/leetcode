from collections import deque, defaultdict
from typing import List


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        queue = deque([source])
        visited = {source}

        while queue:
            cur_node = queue.popleft()
            if cur_node == destination:
                return True
            for node in graph[cur_node]:
                if node not in visited:
                    visited.add(node)
                    queue.append(node)

        return False
