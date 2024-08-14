from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("White")
        self.penup()
        self.hideturtle()
        self.goto(0,270)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score={self.score}",move=False,align="center",font=('Arial',22,'normal'))  

    def game_over(self):
            self.goto(0,0)
            self.write(f"GAME OVER",move=False,align="center",font=('Arial',22,'normal'))  

    def increase_score(self):
        self.score+=1
        self.update_score()



