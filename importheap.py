import heapq 
import time 
 
class Node: 
    def __init__(self, position, parent=None): 
        self.position = position 
        self.parent = parent 
        self.g = 0 
        self.h = 0 
        self.f = 0 
 
def heuristic(a, b): 
    return abs(a[0] - b[0]) + abs(a[1] - b[1]) 
 
def display_maze(maze, start=None, goal=None, path=None, visited=None): 
    print("\nMaze Layout:") 
    for i in range(len(maze)): 
        for j in range(len(maze[0])): 
            pos = (i, j) 
            if pos == start: 
                print("S", end=" ") 
            elif pos == goal: 
                print("G", end=" ") 
            elif path and pos in path: 
                print("*", end=" ") 
            elif visited and pos in visited: 
                print(".", end=" ") 
            elif maze[i][j] == 1: 
                print("#", end=" ") 
            else: 
                print(" ", end=" ") 
        print() 
 
def a_star_search(maze, start, goal, visualize=False): 
    open_list = [] 
    closed_list = set() 
    start_node = Node(start) 
    goal_node = Node(goal) 
    open_list.append(start_node) 
    step = 1 
 
    while open_list: 
        current_node = min(open_list, key=lambda node: node.f) 
        open_list.remove(current_node) 
        closed_list.add(current_node.position) 
 
        if visualize: 
            print(f"\nStep {step}: Exploring {current_node.position}") 
            display_maze(maze, start, goal, visited=closed_list) 
            time.sleep(0.2) 
            step += 1 
 
        if current_node.position == goal_node.position: 
            path = [] 
            while current_node: 
                path.append(current_node.position) 
                current_node = current_node.parent 
            return path[::-1] 
 
        for dx, dy in [(0,1),(1,0),(0,-1),(-1,0)]: 
            x, y = current_node.position[0]+dx, current_node.position[1]+dy 
            if 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] == 0: 
                if (x, y) in closed_list: 
                    continue 
                child = Node((x, y), current_node) 
                child.g = current_node.g + 1 
                child.h = heuristic(child.position, goal_node.position) 
                child.f = child.g + child.h 
                if any(o.position == child.position and o.f <= child.f for o in open_list): 
                    continue 
                open_list.append(child) 
    return None 
 
def input_maze(): 
    rows = int(input("Enter number of rows: ")) 
    cols = int(input("Enter number of columns: ")) 
    maze = [] 
    print("Enter the maze row by row (0 for path, 1 for wall):") 
    for i in range(rows): 
        while True: 
            row = list(map(int, input(f"Row {i+1}: ").split())) 
            if len(row) == cols and all(x in (0,1) for x in row): 
                maze.append(row) 
                break 
            print(f"Please enter exactly {cols} values (0 or 1).") 
    display_maze(maze) 
    return maze 
 
def dynamic_update(maze): 
    print("Enter positions to toggle walls (row col), or '-1 -1' to stop:") 
    while True: 
        r, c = map(int, input("Position: ").split()) 
        if r == -1 and c == -1: 
            break 
        if 0 <= r < len(maze) and 0 <= c < len(maze[0]): 
            maze[r][c] = 1 - maze[r][c] 
            print("Updated Maze:") 
            display_maze(maze) 
        else: 
            print("Invalid position!") 
 
def main(): 
    maze = [] 
    while True: 
        print("\n=== A* MAZE NAVIGATION SYSTEM ===") 
        print("1. Input New Maze") 
        print("2. Solve Static Maze") 
        print("3. Solve Dynamic Maze") 
        print("4. Exit") 
        choice = input("Enter your choice (1–4): ") 
 
        if choice == '1': 
            maze = input_maze() 
        elif choice == '2': 
            if not maze: 
                print("Please input the maze first.") 
                continue 
            start = tuple(map(int, input("Enter start position (row col): ").split())) 
            goal = tuple(map(int, input("Enter goal position (row col): ").split())) 
            visualize = input("Visualize search process? (y/n): ").lower() == 'y' 
            path = a_star_search(maze, start, goal, visualize) 
            if path: 
                print("\nPath Found:", path) 
                display_maze(maze, start, goal, path=path) 
            else: 
                print("No path found!") 
        elif choice == '3': 
            if not maze: 
                print("Please input the maze first.") 
                continue 
            print("\nCurrent Maze:") 
            display_maze(maze) 
            dynamic_update(maze) 
            start = tuple(map(int, input("Enter start position (row col): ").split())) 
            goal = tuple(map(int, input("Enter goal position (row col): ").split())) 
            visualize = input("Visualize search process? (y/n): ").lower() == 'y' 
            path = a_star_search(maze, start, goal, visualize) 
            if path: 
                print("\nPath After Dynamic Update:", path) 
                display_maze(maze, start, goal, path=path) 
            else: 
                print("No path found!") 
        elif choice == '4': 
            print("Exiting A* Maze Navigation System. Thank you!") 
            break 
        else: 
            print("Invalid choice! Enter 1–4.") 
 
main() 
  
