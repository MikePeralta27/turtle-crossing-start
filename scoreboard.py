from turtle import Turtle

FONT = ("Courier", 24, "normal")
GAME_OVER = "GAME OVER"


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 1
        self.create_scoreboard()

    def create_scoreboard(self) -> None:
        self.goto(-280, 260)
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def game_over(self) -> None:
        self.goto(0, 0)
        self.write(GAME_OVER, align="center", font=FONT)

    def increase_level(self) -> None:
        self.level += 1
        self.clear()
        self.create_scoreboard()
