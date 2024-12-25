from heapq import heappush, heappop
from typing import List, Tuple, Dict, Set

def parse_maze(maze_str: str) -> Tuple[List[List[str]], Tuple[int, int], Tuple[int, int]]:
    """Convert maze string to 2D list and find start/end positions."""
    maze = [list(line) for line in maze_str.strip().split('\n')]
    start = end = None
    
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 'S':
                start = (i, j)
            elif maze[i][j] == 'E':
                end = (i, j)
                
    return maze, start, end

def get_turn_cost(current_dir: int, next_dir: int) -> int:
    """Calculate turn cost based on direction change."""
    if current_dir == next_dir:  # No turn
        return 0
    
    diff = (next_dir - current_dir) % 4
    if diff in (1, 3):  # 90-degree turn (clockwise or counterclockwise)
        return 1000
    
    return 0

def get_neighbors_with_directions(pos: Tuple[int, int], current_dir: int, 
                                maze: List[List[str]]) -> List[Tuple[int, int, int]]:
    """Get valid neighboring positions with their direction indices, excluding the opposite direction."""
    row, col = pos
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
    neighbors = []
    
    for dir_idx, (dx, dy) in enumerate(directions):
        # Skip the opposite direction
        if (dir_idx + 2) % 4 == current_dir:
            continue
            
        new_row, new_col = row + dx, col + dy
        if (0 <= new_row < len(maze) and 
            0 <= new_col < len(maze[0]) and 
            maze[new_row][new_col] != '#'):
            neighbors.append((new_row, new_col, dir_idx))
            
    return neighbors

def dijkstra(maze: List[List[str]], start: Tuple[int, int], end: Tuple[int, int]) -> Tuple[List[Tuple[int, int]], int]:
    """Optimized version of Dijkstra's algorithm for maze solving. Returns path and total cost."""
    rows, cols = len(maze), len(maze[0])
    
    # Initialize distances with infinity for all positions and directions
    # Format: distances[(row, col, direction)] = (cost, previous_pos, previous_dir)
    distances = {}
    
    # Priority queue entries: (cost, pos, direction)
    pq = []
    
    # Initialize starting position with all possible directions
    for direction in range(4):
        distances[(start[0], start[1], direction)] = 0
        heappush(pq, (0, start, direction))
    
    while pq:
        current_cost, current_pos, current_dir = heappop(pq)
        
        # If we've reached the end, reconstruct and return the path
        if current_pos == end:
            return current_cost  # Return both path and total cost
        
        # Skip if we've found a better path to this state
        state = (current_pos[0], current_pos[1], current_dir)
        if current_cost > distances[state]:
            continue
        
        # Check neighbors
        for next_row, next_col, next_dir in get_neighbors_with_directions(current_pos, current_dir, maze):
            next_pos = (next_row, next_col)
            next_state = (next_row, next_col, next_dir)
            
            # Calculate new cost
            turn_cost = get_turn_cost(current_dir, next_dir)
            step_cost = 1
            new_cost = current_cost + turn_cost + step_cost
            
            # Update distance if we found a better path
            current_best = distances.get(next_state, float('inf'))
            if new_cost < current_best:
                distances[next_state] = new_cost
                heappush(pq, (new_cost, next_pos, next_dir))
    
    return float('inf')  # No path found


def solve_maze(maze_str: str) -> str:
    """Main function to solve the maze and return the solution with cost."""
    maze, start, end = parse_maze(maze_str)
    total_cost = dijkstra(maze, start, end)
    
    return total_cost

# Example usage
maze_str = open("smallinput.txt", "r").read()

# Get and print solution
solution = solve_maze(maze_str)
print(solution)