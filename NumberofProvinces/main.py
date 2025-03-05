from collections import deque
from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        length = len(isConnected)
        visited = set()
        components = []

        def bfs(start):
            queue = deque([start])
            visited.add(start)
            comp = []

            while queue:
                cur_node = queue.popleft()
                comp.append(cur_node)

                for nei in range(length):
                    if isConnected[cur_node][nei] == 1 and nei not in visited:
                        visited.add(nei)
                        queue.append(nei)
            return comp

        for node in range(length):
            if node not in visited:
                components.append(bfs(node))

        return len(components)
