import turtle
import math

import copy
window = turtle.Screen()
window.bgcolor("black")
window.title("Maze Game")
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
    def move_up(self):
        x = self.xcor() 
        y = self.ycor() +24
        if (x ,y) not in walls :
            self.goto(x , y)

    def move_down(self):
        x = self.xcor() 
        y = self.ycor() -24
        if (x ,y) not in walls :
            self.goto(x , y)
    def move_left(self):
        x = self.xcor() -24
        y = self.ycor() 
        if (x ,y) not in walls :
            self.goto(x , y)
        
    def move_right(self):
        x = self.xcor() +24
        y = self.ycor() 
        if (x ,y) not in walls :
            self.goto(x , y)

    def is_collision(self,other):
        x = self.xcor() - other.xcor()
        y = self.ycor() - other.ycor()
        distance = math.sqrt( x**2 + y**2)

        if distance < 5 :
            return True
        else:
            return False

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
        


maze1 = [
['X', 'P', '', '', '', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '', '', 'T', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
['X', '', '', 'X', '', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '', '', '', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
['X', '', '', 'X', '', '', '', '', '', 'X', 'X', 'X', 'X', 'X', '', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
['X', '', '', 'X', 'X', 'X', '', '', '', '', '', '', '', '', '', '', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
['X', 'X', '', '', '', 'X', '', '', 'X', 'X', 'X', '', '', '', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
['X', 'X', '', '', '', '', 'X', 'X', 'X', 'X', 'X', '', '', '', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
['X', 'X', 'X', 'X', '', 'X', 'X', 'X', 'X', 'X', '', '', '', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
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
['X', 'X', 'X', 'X', 'X', 'X', 'X', '', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
['X', 'X', 'X', 'X', '', '', '', '', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
['X', 'X', 'X', 'X', '', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']]

def setup_maze(maze):
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
            


# class Initialization
pen = Pen()
player = Player()
treasure = Treasure()

walls = []
# Game setup
setup_maze(maze1)


# Keyboard
turtle.listen()
turtle.onkey(player.move_left , "Left")
turtle.onkey(player.move_right , "Right")
turtle.onkey(player.move_up , "Up")
turtle.onkey(player.move_down , "Down")

window.tracer(0)
while True:

    if player.is_collision(treasure):
        print("You Win")
        treasure.destroy()
        break
    window.update()
    pass
