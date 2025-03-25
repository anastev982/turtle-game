import random
from turtle import Turtle
from player import Player

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

screen = Turtle().getscreen()


class CarManager:
    def __init__(self):
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE

        for _ in range(15):
            car = Turtle("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            car.color(random.choice(COLORS))
            car.goto(290, random.randint(-250, 250))
            car.speed = random.randint(1,5)
            self.cars.append(car)

    def move(self):
        for car in self.cars:
            new_x = car.xcor() - car.speed
            car.goto(new_x, car.ycor())

    def increase_speed(self):
        self.speed += MOVE_INCREMENT

    def off_screen(self):
        for car in self.cars:
            if car.xcor() < -320:
                car.goto(290, random.randint(-250, 250))

    def reset_game(self):
        for car in self.cars:
            car.setposition(290, (random.randint(-250, 250)))
            print("New Game")

    def collision(self, player):
        for car in self.cars:
            distance = car.distance(player)

            if distance < 20:
                return True
        return False

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("bold"))


