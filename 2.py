import heapq  # Importing heapq module for priority queue functionality

def heuristic(node, goal):
    """
    Heuristic function to estimate the cost from a given node to the goal node.
    """
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

def astar(grid, start, goal):
    """
    A* algorithm implementation to find the shortest path from start to goal in a grid.
    """
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Possible movement directions (right, left, down, up)
    open_list = [(0, start)]  # Priority queue to store nodes being considered, initialized with start node
    came_from = {}  # Dictionary to store parent nodes for reconstructing the path
    g_score = {start: 0}  # Dictionary to store the cost of reaching each node from the start node
    
    while open_list:
        current_cost, current_node = heapq.heappop(open_list)  # Pop the node with the lowest cost from the priority queue
        
        if current_node == goal:  # If the current node is the goal node, reconstruct and return the path
            path = []
            while current_node in came_from:
                path.insert(0, current_node)
                current_node = came_from[current_node]
            return path
        
        for dx, dy in directions:  # Explore neighbors of the current node
            neighbor = current_node[0] + dx, current_node[1] + dy  # Calculate neighbor coordinates
            new_cost = g_score[current_node] + 1  # Calculate the cost of reaching the neighbor
            
            if (0 <= neighbor[0] < len(grid) and  # Check if the neighbor is within the grid boundaries
                0 <= neighbor[1] < len(grid[0]) and
                grid[neighbor[0]][neighbor[1]] != '#'):  # Check if the neighbor is not an obstacle ('#')
                
                if (neighbor not in g_score or  # If the neighbor is not yet visited or a better path is found
                    new_cost < g_score[neighbor]):
                    
                    g_score[neighbor] = new_cost  # Update the cost of reaching the neighbor
                    priority = new_cost + heuristic(neighbor, goal)  # Calculate priority based on cost and heuristic
                    heapq.heappush(open_list, (priority, neighbor))  # Add the neighbor to the priority queue
                    came_from[neighbor] = current_node  # Record the parent node for reconstructing the path
    
    return None  # If no path is found, return None

# Example usage:
grid = [
    ['#', '#', '#', '#', '#', '#', '#', '#'],
    ['#', 'S', ' ', ' ', '#', ' ', ' ', '#'],
    ['#', ' ', '#', ' ', '#', ' ', '#', '#'],
    ['#', ' ', '#', ' ', '#', ' ', ' ', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', '#', '#'],
    ['#', '#', '#', '#', '#', 'G', '#', '#'],
    ['#', '#', '#', '#', '#', '#', '#', '#']
]

start = (1, 1)  # Start position
goal = (5, 5)  # Goal position

path = astar(grid, start, goal)  # Find path using A* algorithm
if path:
    print("Path found:", path)  # If a path is found, print it
else:
    print("No path found")  # If no path is found, print a message
