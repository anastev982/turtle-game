import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

player = Player()
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.tracer(0)

all_turtles = screen.turtles()
for turtle in all_turtles:
    if turtle.shape() != "turtle" and turtle.pos() == (0, 0):
        turtle.clear()
        turtle.hideturtle()
        turtle.getscreen()._delete(turtle._screen)
        print(f"Unwanted  Turtle at {turtle.pos()} deleted.")

car_manager = CarManager()
scoreboard = Scoreboard()


def move_player():
    player.move()


screen.listen()
screen.onkey(move_player, "space")

game_is_on = True
level_completed = False

while game_is_on:
    car_manager.move()
    screen.update()

    if player.win():
        if not level_completed:
            scoreboard.player_win()
            print("You Won!")
            # car_manager.reset_game()
            player.reset_position()
            level_completed = True

            scoreboard.update_level()
            time.sleep(1)
            print("Level Up")
            time.sleep(1)

        if player.ycor() < 280:
            level_completed = False

    # car_manager.move()

    if car_manager.off_screen():
        car_manager.reset_game()

    if car_manager.collision(player):
        print("Game Over!")
        scoreboard.game_over()
        game_is_on = False
        screen.update()

    time.sleep(0.1)

screen.mainloop()
