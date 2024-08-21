from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.add_eyes()  # Add eyes to the head

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")  # Keep the square shape for both head and body
        new_segment.color("white")  # Same color for the entire snake
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def add_eyes(self):
        """Add eyes to the snake's head."""
        # Left eye
        self.left_eye = Turtle("circle")
        self.left_eye.color("black")
        self.left_eye.shapesize(stretch_wid=0.2, stretch_len=0.2)  # Small size for the eyes
        self.left_eye.penup()
        self.left_eye.goto(self.head.xcor() - 7, self.head.ycor() + 7)  # Position the left eye on the head

        # Right eye
        self.right_eye = Turtle("circle")
        self.right_eye.color("black")
        self.right_eye.shapesize(stretch_wid=0.2, stretch_len=0.2)  # Small size for the eyes
        self.right_eye.penup()
        self.right_eye.goto(self.head.xcor() + 7, self.head.ycor() + 7)  # Position the right eye on the head

    def move_eyes(self):
        """Move the eyes with the snake's head."""
        self.left_eye.goto(self.head.xcor() - 7, self.head.ycor() + 7)  # Adjust the eye's position
        self.right_eye.goto(self.head.xcor() + 7, self.head.ycor() + 7)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
        self.move_eyes()  # Ensure the eyes move with the head

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
