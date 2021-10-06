import turtle
import math

import copy

window = turtle.Screen()
window.bgcolor("black")
window.title("Maze Solver")
window.setup(700 , 700)

class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)



class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("circle")
        self.color("red")
        self.penup()
        self.speed(0)

class Treasure(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("triangle")
        self.color("gold")
        self.penup()
        self.speed(0)
        


    def destroy(self):
        self.goto(2000,2000)
        self.hideturtle()

class Path(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("triangle")
        self.color("Green")
        self.penup()
        self.speed(2)

maze1 = [
['X', 'P', '', '', '', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '', '', '', '', ''],
['X', '', '', 'X', '', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '', 'X', 'X', 'X', 'X'],
['X', '', '', 'X', '', '', '', '', '', '', '', '', '', '', '', '', 'X', 'X', 'X', 'X', 'X', 'X', '', 'X', 'X'],
['X', '', '', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '', '', '', '', '', '', '', '', '', '', '', 'X', 'X'],
['X', 'X', '', '', '', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '', '', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
['X', 'X', '', '', '', '', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
['X', 'X', 'X', 'X', '', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
['X', '', '', '', '', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
['X', 'X', 'X', 'X', '', '', '', '', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
['X', 'X', 'X', 'X', '', 'X', '', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
['X', 'X', 'X', 'X', '', 'X', '', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
['X', 'X', 'X', 'X', '', 'X', '', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
['X', 'X', 'X', 'X', '', '', '', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
['X', 'X', 'X', 'X', '', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
['X', 'X', 'X', 'X', '', '', '', '', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
['X', 'X', 'X', 'X', 'X', 'X', '', '', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
['X', 'X', 'X', 'X', 'X', 'X', 'X', '', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
['X', 'X', 'X', 'X', 'X', 'X', 'X', '', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
['X', 'X', 'X', 'X', 'X', 'X', 'X', '', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
['X', 'X', 'X', 'X', 'X', 'X', 'X', '', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
['X', 'X', 'X', 'X', 'X', 'X', 'X', '', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
['X', 'X', 'X', 'X', 'X', 'X', 'X', '', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
['X', 'X', 'X', 'X', 'X', 'X', 'X', 'T', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
['X', 'X', 'X', 'X', '', '', '', '', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
['X', 'X', 'X', 'X', '', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']]


pen = Pen()
player = Player()
treasure = Treasure()
path = Path()
walls = []


def dfs(maze,i,j):
    if i < 0 or j < 0 or i >= len(maze) or j >= len(maze[0])  or (maze[i][j] == "X" ) or maze[i][j] == "-":
        return
    if maze[i][j] == "T":

        return True

    maze[i][j] = "-"

    path.goto(-288 + (j*24) ,  288 - (i*24))
    path.stamp()

    
        
    dfs(maze,i+1,j)
    dfs(maze,i-1,j)
    dfs(maze,i,j+1)
    dfs(maze,i,j-1)



def setup_solved_maze(maze):
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            char = maze[row][col]
            screen_row = 288 - (row*24)
            screen_col = -288 + (col*24)
            if char == "X":
                pen.goto(screen_col , screen_row)
                pen.stamp()
                walls.append((screen_col , screen_row))
            if char == "P" :
                player.goto(screen_col,screen_row)
            if char == "T":
                treasure.goto(screen_col,screen_row)

setup_solved_maze(maze1)

dfs(maze1,0,1)
#print(maze1)
window.tracer(0)
while True:

    # if player.is_collision(treasure):
    #     print("You Win")
    #     treasure.destroy()
    #     break
    window.update()
    pass