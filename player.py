import time
from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        print("Player initialized as a Turtle")
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.goto(0, -280)
        self.setheading(90)

    def move(self):
        self.forward(10)

    def win(self):
        if self.ycor() >= FINISH_LINE_Y:
            print("You Won!")
            return True
        return False

    def reset_position(self):
        self.goto(STARTING_POSITION)

    def level_completed(self):
        if self.ycor() > 280:
            self.reset()
            time.sleep(0.1)
            #self.level += 1

