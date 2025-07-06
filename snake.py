import turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE=20
RIGHT=0
UP=90
LEFT=180
DOWN=270

class Snake:

    def __init__(self):
        self.segments=[]
        self.create_snake()#When each object is created,this itself create a new snake class
        self.head=self.segments[0]#After creating the snake,set the first segment as head because it is frequently using

    def create_snake(self):
        for pos in STARTING_POSITIONS:
            self.add_segment(pos)

    def add_segment(self,position):
        new_segment = turtle.Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)


    def extend_snake(self):
        self.add_segment(self.segments[-1].position())


    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def moveUp(self):
        if self.head.heading() != DOWN:#Can't move backwards
            self.head.setheading(90)

    def moveDown(self):
        if self.head.heading()!= UP:#Can't move backwards
            self.head.setheading(270)

    def moveRight(self):
        if self.head.heading()!= LEFT:#Can't move backwards
            self.head.setheading(0)

    def moveLeft(self):
        if self.head.heading()!=RIGHT:#Can't move backwards
            self.head.setheading(180)
