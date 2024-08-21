from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        random_shape = random.choice(["circle", "square", "triangle", "turtle"])
        random_color = random.choice(["blue", "red", "green", "yellow", "purple", "orange"])
        self.shape(random_shape)  # Random shape
        self.color(random_color)  # Random color
        self.goto(random_x, random_y)
