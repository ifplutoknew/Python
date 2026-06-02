import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox

class cube(object):
    rows = 20
    w= 500
    def __init__(self,start,dirnx=1,dirny=0,color=(255,0,0)):
        self.pos = start
        self.dirnx = 1
        self.dirny = 0
        self.color = color


    def move(self, dirnx, dirny):
        self.dirnx = dirnx
        self.dirny = dirny
        self.pos = (self.pos[0] + self.dirnx, self.pos[1] + self.dirny)  #update the position of the cube based on its current direction


    def draw(self, surface, eyes=False):
        dis = self.w // self.rows    #size of each grid cell
        i = self.pos[0]             #x-coordinate of the cube's position
        j = self.pos[1]             #y-coordinate of the cube's position

        pygame.draw.rect(surface, self.color, (i*dis+1,j*dis+1, dis-2, dis-2)) #draw the cube as a rectangle on the surface
        if eyes:        #if the eyes parameter is True, draw the eyes on the cube (used for the head of the snake)
            centre = dis//2
            radius = 3
            circleMiddle = (i*dis + centre - radius, j*dis + 8) #position of the left eye
            circleMiddle2 = (i*dis + dis - radius*2, j*dis + 8) #position of the right eye
            pygame.draw.circle(surface, (0,0,0), circleMiddle, radius) #draw the left eye as a circle
            pygame.draw.circle(surface, (0,0,0), circleMiddle2, radius) #draw the right eye as a circle



class snake(object):
    body = []     #list to keep track of the positions of the snake's body segments
    turns = {}    #dictionary to keep track of the turns made by the snake

    def __init__(self, color, pos):
        self.color = color
        self.head = cube(pos)        #the head of the snake is represented as a cube
        self.body.append(self.head)  #add the head to the body list
        self.dirnx = 0               #initial direction of the snake (x-axis)
        self.dirny = 1               #initial direction of the snake (y-axis)

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  #if the user clicks the close button, quit the game
                pygame.quit()
            
            keys = pygame.key.get_pressed()   #get the state of all keyboard buttons
            for key in keys:
                if keys[pygame.K_LEFT]: #if the left arrow key is pressed
                    self.dirnx = -1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny] #store the turn in the turns dictionary with the current position of the head as the key
                    
                
                elif keys[pygame.K_RIGHT]: #if the right arrow key is pressed
                    self.dirnx = 1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny] #store the turn in the turns dictionary with the current position of the head as the key

                elif keys[pygame.K_UP]: #if the up arrow key is pressed
                    self.dirnx = 0
                    self.dirny = -1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny] #store the turn in the turns dictionary with the current position of the head as the key
                
                elif keys[pygame.K_DOWN]: #if the down arrow key is pressed
                    self.dirnx = 0
                    self.dirny = 1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny] #store the turn in the turns dictionary with the current position of the head as the key
                
            for i, c in enumerate(self.body): #iterate through each segment of the snake's body
                p = c.pos[:]                     #get the current position of the segment
                if p in self.turns:              #if the current position of the segment is in the turns dictionary, it means the segment needs to turn
                    turn = self.turns[p]         #get the direction of the turn from the turns dictionary
                    c.move(turn[0], turn[1])     #move the segment in the direction of the turn
                    if i == len(self.body)-1:    #if this is the last segment of the body, remove the turn from the turns dictionary
                        self.turns.pop(p)
                else:                                        #if the current position of the segment is not in the turns dictionary, it means the segment needs to continue moving in the same direction
                    if c.dirnx == -1 and c.pos[0] <= 0:      #if the segment is moving left and reaches the left edge of the window, wrap around to the right edge
                        c.pos = (c.rows-1, c.pos[1])
                    elif c.dirnx == 1 and c.pos[0] >= c.rows-1:    #if the segment is moving right and reaches the right edge of the window, wrap around to the left edge
                        c.pos = (0, c.pos[1])
                    elif c.dirny == 1 and c.pos[1] >= c.rows-1:    
                        c.pos = (c.pos[0], 0)                      
                    elif c.dirny == -1 and c.pos[1] <= 0:         
                        c.pos = (c.pos[0], c.rows-1)
                    else:
                        c.move(c.dirnx, c.dirny) #move the segment in its current direction      

    def reset(self, pos):
        self.head = cube(pos)        #reset the head of the snake to the initial position
        self.body = []              #clear the body list
        self.body.append(self.head)  #add the head back to the body list
        self.turns = {}             #clear the turns dictionary
        self.dirnx = 0              #reset the direction of the snake (x-axis)
        self.dirny = 1              #reset the direction of the snake (y-axis)

    def addCube(self):
        tail = self.body[-1] #last segment of the snake's body (the tail)
        dx, dy = tail.dirnx, tail.dirny #current direction of the tail

        if dx == 1 and dy == 0:   #if the tail is moving right, add a new segment to the left of the tail
            self.body.append(cube((tail.pos[0]-1, tail.pos[1])))
        elif dx == -1 and dy == 0:    #if the tail is moving left, add a new segment to the right of the tail
            self.body.append(cube((tail.pos[0]+1, tail.pos[1])))
        elif dx == 0 and dy == 1:     #if the tail is moving down, add a new segment above the tail
            self.body.append(cube((tail.pos[0], tail.pos[1]-1)))
        elif dx == 0 and dy == -1:    #if the tail is moving up, add a new segment below the tail
            self.body.append(cube((tail.pos[0], tail.pos[1]+1)))
        
        self.body[-1].dirnx = dx  #set the direction of the new segment to be the same as the tail
        self.body[-1].dirny = dy

    def draw(self, surface):
        for i, c in enumerate(self.body):
            if i == 0:     #if this is the head of the snake, draw it with eyes
                c.draw(surface, True)
            else:           
                c.draw(surface)    #if this is a body segment, draw it without eyes


def drawGrid(w, rows, surface):
    sizeBetween = w // rows  #size of each grid cell
    x = 0
    y = 0
    for l in range(rows):
        x = x + sizeBetween
        y = y + sizeBetween
        pygame.draw.line(surface, (255,255,255), (x,0),(x,w)) #draw vertical lines
        pygame.draw.line(surface, (255,255,255), (0,y),(w,y)) #draw horizontal lines

def redrawWindow(surface):
    global rows, width, s, snack
    surface.fill((0,0,0))         #fill the window with black color
    s.draw(surface)              #draw the snake on the surface
    snack.draw(surface)          #draw the snack on the surface
    drawGrid(width, rows, surface)         #draw the grid on the surface
    pygame.display.update()   #update the display after drawing everything

def randomSnack(rows, item):
    positions = item.body
    while True:
        x = random.randrange(rows)   #generate a random x-coordinate for the snack
        y = random.randrange(rows)   #generate a random y-coordinate for the snack
        if len(list(filter(lambda z: z.pos == (x,y), positions))) > 0: #check if the generated position is already occupied by the snake's body
            continue
        else:
            break
    
    return (x,y)   #return the generated position for the snack

def message_box(subject, content):
    root = tk.Tk()   #create a Tkinter root window
    root.attributes("-topmost", True)  #set the window to be always on top
    root.withdraw()  #hide the root window
    messagebox.showinfo(subject, content)  #show a message box with the given subject and content
    try:
        root.destroy()  #destroy the root window after the message box is closed
    except:
        pass

def main():
    global width, rows, s, snack
    width = 500
    rows  = 20
    win = pygame.display.set_mode((width, width)) #create a window of size 500x500
    s = snake((255,0,0), (10,10)) #initial position of the snake
    snack = cube(randomSnack(rows, s), color=(0,255,0)) #create a snack at a random position green color
    flag = True
    clock = pygame.time.Clock() #clock object to control the speed of the game

    while flag:
        pygame.time.delay(80)   #delay of 80 milliseconds
        clock.tick(20)          #20 frames per second
        s.move()   #move the snake based on user input
        if s.body[0].pos == snack.pos:     #if the head of the snake hits the snack
            s.addCube()                    #add a new segment to the snake's body
            snack = cube(randomSnack(rows, s), color=(0,255,0))
        
        for x in range(len(s.body)):
            if s.body[x].pos in list(map(lambda z: z.pos, s.body[x+1:])): #check if the head collides with other segments of the body
                print('Score: ',len(s.body)) #print the score (length of the snake)
                message_box('Game Over', f'Your score is: {len(s.body)}')
                s.reset((10,10)) #reset the snake to the initial position
                break

        redrawWindow(win)




if __name__ == "__main__":
    main()