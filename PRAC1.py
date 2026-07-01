from collections import deque
import time

graph = {
    "Andheri": ["Jogeshwari", "Vile Parle"],
    "Jogeshwari": ["Goregaon"],
    "Vile Parle": ["Santacruz"],
    "Goregaon": ["Ram Mandir"],
    "Santacruz": ["Khar Road"],
    "Ram Mandir": ["Bandra"],
    "Khar Road": ["Bandra"],
    "Bandra": ["Mahim"],
    "Mahim": ["Matunga Road"],
    "Matunga Road": ["Dadar"],
    "Dadar": []
}

# ---------------- BFS ----------------

def bfs(graph, start, goal):
    visited = set()
    queue = deque([(start, [start])])

    print("BFS Traversal:\n")

    while queue:
        node, path = queue.popleft()

        if node not in visited:
            print(node)
            visited.add(node)

            if node == goal:
                print("\nShortest Path:")
                print(" -> ".join(path))
                return path

            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))

# ---------------- DFS ----------------

def iterative_dfs(graph, start, goal):
    visited = set()
    stack = [(start, [start])]

    print("\nDFS Traversal:\n")

    while stack:
        node, path = stack.pop()

        if node not in visited:
            print(node)
            visited.add(node)

            if node == goal:
                print("\nPath Found:")
                print(" -> ".join(path))
                return path

            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor]))

# Source and Destination

source = "Andheri"
destination = "Dadar"

print("Source:", source)
print("Destination:", destination)
print("-" * 40)

bfs_path = bfs(graph, source, destination)

print("\n" + "-" * 40)

dfs_path = iterative_dfs(graph, source, destination)

# ---------------- Performance Comparison ----------------

start_time = time.time()
bfs(graph, source, destination)
bfs_time = time.time() - start_time

start_time = time.time()
iterative_dfs(graph, source, destination)
dfs_time = time.time() - start_time

print("\n===== BFS vs DFS Comparison =====")

print("\nBFS Path:", " -> ".join(bfs_path))
print("DFS Path:", " -> ".join(dfs_path))

print("\nExecution Time:")
print("BFS Time:", bfs_time)
print("DFS Time:", dfs_time)

print("\nConclusion:")
print("BFS gives the shortest path in an unweighted graph.")
print("DFS explores one branch completely before backtracking and may not always find the shortest path.")