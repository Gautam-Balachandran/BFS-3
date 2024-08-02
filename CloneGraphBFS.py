# Time Complexity : O(v + e), where v is the number of vertices and e is the
# number of edges
# Space Complexity : O(v)
from collections import deque

class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node):
        if node is None:
            return None

        # Use a map to save the cloned nodes.
        visited = {}
        # Initialize the queue for BFS.
        queue = deque([node])
        # Clone the root node.
        visited[node] = Node(node.val, [])

        # Start BFS traversal.
        while queue:
            n = queue.popleft()
            # Iterate through the neighbors.
            for neighbor in n.neighbors:
                if neighbor not in visited:
                    # Clone the neighbor and put it in the map.
                    visited[neighbor] = Node(neighbor.val, [])
                    # Add the neighbor to the queue for further traversal.
                    queue.append(neighbor)
                # Add the cloned neighbor to the current node's neighbors.
                visited[n].neighbors.append(visited[neighbor])

        return visited[node]

# Examples to test the code

# Example 1: A simple graph with two connected nodes
node1 = Node(1)
node2 = Node(2)
node1.neighbors = [node2]
node2.neighbors = [node1]

sol = Solution()
cloned_graph = sol.cloneGraph(node1)
print("Example 1: ", [(n.val, [nei.val for nei in n.neighbors]) for n in [cloned_graph, cloned_graph.neighbors[0]]]) # Output : [(1, [2]), (2, [1])]

# Example 2: A graph with three nodes in a triangle
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node1.neighbors = [node2, node3]
node2.neighbors = [node1, node3]
node3.neighbors = [node1, node2]

sol = Solution()
cloned_graph = sol.cloneGraph(node1)
print("Example 2: ", [(n.val, [nei.val for nei in n.neighbors]) for n in [cloned_graph, cloned_graph.neighbors[0], cloned_graph.neighbors[1]]]) # Output : [(1, [2, 3]), (2, [1, 3]), (3, [1, 2])]

# Example 3: A graph with a single node that has a self-loop
node1 = Node(1)
node1.neighbors = [node1]

sol = Solution()
cloned_graph = sol.cloneGraph(node1)
print("Example 3: ", [(n.val, [nei.val for nei in n.neighbors]) for n in [cloned_graph]]) # Output : [(1, [1])]