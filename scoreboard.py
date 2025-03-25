from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-270, 270)
        self.update_scoreboard()

    def player_win(self):
        self.update_scoreboard()
        self.hideturtle()
        self.reset()
        # self.level += 1

    def update_scoreboard(self):
        print("Updating scoreboard with Level:", self.level)
        self.clear()
        self.write(f"Level: {self.level}",
                   font=("Courier", 18, "normal"),
                   align="left")

    def update_level(self):
        self.goto(-270, 270)
        self.clear()
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Courier", 18, "normal"))
