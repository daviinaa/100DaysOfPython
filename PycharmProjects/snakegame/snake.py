from turtle import Turtle
# starting positions for the 3 snake blocks (mainseg)
STARING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

# defining the snake class


class Snake:
    def __init__(self,):
        self.main_seg = []
        self.create_snake()
        self.head = self.main_seg[0]

    def create_snake(self):
        for position in STARING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        snake_seg = Turtle("square")
        snake_seg.color("white")
        snake_seg.pu()
        snake_seg.goto(position)
        self.main_seg.append(snake_seg)

    def reset(self):
        for seg in self.main_seg:
            seg.goto(1000, 1000)
        self.main_seg.clear()
        self.create_snake()
        self.head = self.main_seg[0]

    def extend(self):
        self.add_segment(self.main_seg[-1].position())

    def move(self):
        # this range takes in the len of the main_seg(which is a list) and starts there, then moves by -1, and stops at 0.
        for seg_num in range(len(self.main_seg) - 1, 0, -1):
            new_x = self.main_seg[seg_num - 1].xcor()
            new_y = self.main_seg[seg_num - 1].ycor()
            # this is saying that the particular snake in the loop should move to the position of the snake in front of it
            self.main_seg[seg_num].goto(new_x, new_y)
        #     get hold of the first segment and move it
        self.head.forward(MOVE_DISTANCE)

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

