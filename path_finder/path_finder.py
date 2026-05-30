#shortest path finder in a maze using breadth first search algorithm
import curses              #for terminal handling
from curses import wrapper #to initialize curses and call the main function
import queue               #for implementing the breadth first search algorithm
import time                #for adding delay in the visualization of the path finding process

maze = [
    ["#", "O", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "X", "#"]
]

def print_maze(maze, stdscr,path=[]): #function to print the maze on the terminal using curses
    BLUE = curses.color_pair(1) #get the color pair 1 for blue text and black background
    RED = curses.color_pair(2) #get the color pair 2 for red text and black background
    
    for i, row in enumerate(maze): #iterate through each row of the maze
        for j, value in enumerate(row): #iterate through each value in the row
            if (i, j) in path:
                stdscr.addstr(i,j*2,'X', RED) #add the value to the terminal at the position (i, j*2) to create a grid-like structure
            else:
                stdscr.addstr(i,j*2,value, BLUE) #add the value to the terminal at the position (i, j*2) to create a grid-like structure

def find_start(maze, start): #function to find the starting point 'O' in the maze and return its coordinates
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if value == start:
                return i, j 
    
    return None



def find_path(maze, stdscr): #function to find the shortest path from the start point 'O' to the end point 'X' using breadth first search algorithm
    start = 'O'
    end = 'X'
    start_pos = find_start(maze, start) #get the coordinates of the starting point 'O'

    q  = queue.Queue() #create a queue to store the positions to be explored
    q.put((start_pos, [start_pos])) #enqueue the starting position and the path taken to reach it

    visited = set() #create a set to keep track of visited positions

    while not q.empty(): #while there are positions to be explored
        current_pos, path  =  q.get() #dequeue the next position and the path taken to reach it
        row, col = current_pos #get the row and column of the current position
        
        stdscr.clear()                #clear the terminal screen
        print_maze(maze,stdscr,path)  #print the maze on the terminal with the current path highlighted
        time.sleep(0.2)               #add a delay of 0.2 seconds to visualize the path finding process
        stdscr.refresh()              #refresh the terminal screen to show the current state of the maze

        if maze[row][col] == end: #if the current position is the end point 'X', return the path taken to reach it
            return path
        
        neighbors = find_neighbors(maze, row, col) #get the valid neighbors of the current position
        for neighbor in neighbors: #iterate through each neighbor
            if neighbor in visited: #if the neighbor has already been visited, skip it
                continue
            r, c = neighbor #get the row and column of the neighbor
            if maze[r][c] == "#": #if the neighbor is a wall, skip it
                continue
            
            new_path =  path + [neighbor]  #create a new path by adding the neighbor to the current path
            q.put((neighbor, new_path))    #enqueue the neighbor and the path taken to reach it
            visited.add(neighbor)          #mark the neighbor as visited
        



def find_neighbors(maze, row, col): #function to find the valid neighbors of a given position in the maze
    neighbors = []
    
    if row > 0:                           #if the current position is not in the first row, check the position above it
        neighbors.append((row-1, col))      #add the position above the current position to the neighbors list
    if row +1 < len(maze):                #if the current position is not in the last row, check the position below it
        neighbors.append((row+1, col))      #add the position below the current position to the neighbors list
    if col > 0:                           #if the current position is not in the first column, check the position to the left of it
        neighbors.append((row, col-1))      #add the position to the left of the current position to the neighbors list
    if col +1 < len(maze[0]):             #if the current position is not in the last column, check the position to the right of it
        neighbors.append((row, col+1))      #add the position to the right of the current position to the neighbors list

    return neighbors



def main(stdscr): #main function to run the path finding algorithm and visualize it using curses
    curses.init_pair(1,curses.COLOR_BLUE, curses.COLOR_BLACK) #initialize color pair 1 with blue text and black background
    curses.init_pair(2,curses.COLOR_RED, curses.COLOR_BLACK)

    find_path(maze, stdscr) #call the find_path function to find the shortest path from 'O' to 'X' and visualize it on the terminal
    stdscr.getch() #wait for user input before starting the path finding algorithm




wrapper(main) #call the main function using wrapper to initialize curses and handle cleanup after the program exits


