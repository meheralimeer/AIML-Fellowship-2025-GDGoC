import matplotlib.pyplot as plt
from collections import defaultdict, deque
import heapq
import time

# Graph representation: Cities and distances (adjacency list with weights)
graph = {
    'Islamabad': {'Rawalpindi': 25, 'Abbottabad': 130},
    'Rawalpindi': {'Islamabad': 25, 'Gujranwala': 170},
    'Abbottabad': {'Islamabad': 130, 'Peshawar': 90},
    'Peshawar': {'Abbottabad': 90, 'Lahore': 380},
    'Gujranwala': {'Rawalpindi': 170, 'Lahore': 70},
    'Lahore': {'Gujranwala': 70, 'Peshawar': 380}
}

# Heuristic: Straight-line distances to Lahore (for informed search)
heuristic = {
    'Islamabad': 370, 'Rawalpindi': 350, 'Abbottabad': 300,
    'Peshawar': 380, 'Gujranwala': 70, 'Lahore': 0
}

# Problem formulation
initial_state = 'Islamabad'
goal_state = 'Lahore'

# BFS Implementation
def bfs(graph, start, goal):
    visited = set()
    queue = deque([(start, [start], 0)])  # (node, path, cost)
    nodes_expanded = 0
    start_time = time.time()
    
    while queue:
        node, path, cost = queue.popleft()
        nodes_expanded += 1
        if node == goal:
            return path, cost, nodes_expanded, time.time() - start_time
        if node not in visited:
            visited.add(node)
            for neighbor, weight in graph[node].items():
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor], cost + weight))
    return None, float('inf'), nodes_expanded, time.time() - start_time

# DFS Implementation
def dfs(graph, start, goal):
    visited = set()
    stack = [(start, [start], 0)]  # (node, path, cost)
    nodes_expanded = 0
    start_time = time.time()
    
    while stack:
        node, path, cost = stack.pop()
        nodes_expanded += 1
        if node == goal:
            return path, cost, nodes_expanded, time.time() - start_time
        if node not in visited:
            visited.add(node)
            for neighbor, weight in graph[node].items():
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor], cost + weight))
    return None, float('inf'), nodes_expanded, time.time() - start_time

# Greedy Best-First Search Implementation
def greedy_bfs(graph, start, goal, heuristic):
    priority_queue = [(heuristic[start], start, [start], 0)]  # (heuristic, node, path, cost)
    visited = set()
    nodes_expanded = 0
    start_time = time.time()
    
    while priority_queue:
        _, node, path, cost = heapq.heappop(priority_queue)
        nodes_expanded += 1
        if node == goal:
            return path, cost, nodes_expanded, time.time() - start_time
        if node not in visited:
            visited.add(node)
            for neighbor, weight in graph[node].items():
                if neighbor not in visited:
                    heapq.heappush(priority_queue, (heuristic[neighbor], neighbor, path + [neighbor], cost + weight))
    return None, float('inf'), nodes_expanded, time.time() - start_time

# A* Search Implementation
def a_star(graph, start, goal, heuristic):
    priority_queue = [(heuristic[start], 0, start, [start])]  # (f = g + h, g, node, path)
    visited = set()
    nodes_expanded = 0
    start_time = time.time()
    
    while priority_queue:
        _, g, node, path = heapq.heappop(priority_queue)
        nodes_expanded += 1
        if node == goal:
            return path, g, nodes_expanded, time.time() - start_time
        if node not in visited:
            visited.add(node)
            for neighbor, weight in graph[node].items():
                if neighbor not in visited:
                    g_new = g + weight
                    f_new = g_new + heuristic[neighbor]
                    heapq.heappush(priority_queue, (f_new, g_new, neighbor, path + [neighbor]))
    return None, float('inf'), nodes_expanded, time.time() - start_time

# Visualization of the search path
def plot_path(path, title):
    if not path:
        print(f"No path found for {title}")
        return
    x = range(len(path))
    y = [1] * len(path)  # Dummy y-values for visualization
    plt.figure(figsize=(10, 2))
    plt.plot(x, y, 'bo-', label='Path')
    for i, city in enumerate(path):
        plt.text(i, 1.01, city, ha='center')
    plt.title(title)
    plt.legend()
    plt.axis('off')
    plt.show()

# Main execution and comparison
def main():
    # Run all algorithms
    bfs_path, bfs_cost, bfs_nodes, bfs_time = bfs(graph, initial_state, goal_state)
    dfs_path, dfs_cost, dfs_nodes, dfs_time = dfs(graph, initial_state, goal_state)
    greedy_path, greedy_cost, greedy_nodes, greedy_time = greedy_bfs(graph, initial_state, goal_state, heuristic)
    a_star_path, a_star_cost, a_star_nodes, a_star_time = a_star(graph, initial_state, goal_state, heuristic)

    # Print results
    print("BFS:", bfs_path, "Cost:", bfs_cost, "Nodes Expanded:", bfs_nodes, "Time:", bfs_time)
    print("DFS:", dfs_path, "Cost:", dfs_cost, "Nodes Expanded:", dfs_nodes, "Time:", dfs_time)
    print("Greedy BFS:", greedy_path, "Cost:", greedy_cost, "Nodes Expanded:", greedy_nodes, "Time:", greedy_time)
    print("A* Search:", a_star_path, "Cost:", a_star_cost, "Nodes Expanded:", a_star_nodes, "Time:", a_star_time)

    # Plot paths
    plot_path(bfs_path, "BFS Path")
    plot_path(dfs_path, "DFS Path")
    plot_path(greedy_path, "Greedy BFS Path")
    plot_path(a_star_path, "A* Search Path")

    # Comparison table
    print("\nComparison Table:")
    print("| Algorithm       | Cost | Nodes Expanded | Time (s) |")
    print("|-----------------|------|----------------|----------|")
    print(f"| BFS            | {bfs_cost} | {bfs_nodes}         | {bfs_time:.4f} |")
    print(f"| DFS            | {dfs_cost} | {dfs_nodes}         | {dfs_time:.4f} |")
    print(f"| Greedy BFS     | {greedy_cost} | {greedy_nodes}         | {greedy_time:.4f} |")
    print(f"| A* Search      | {a_star_cost} | {a_star_nodes}         | {a_star_time:.4f} |")

if __name__ == "__main__":
    main()