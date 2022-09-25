from turtle import Screen, Turtle


STARTING_POSITIONS=[(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE=20
UP=90
DOWN=270
LEFT=180
RIGHT=0



class Snake:
    def __init__(self):
        self.snake_shape=[]
        self.create_snake()
        # 자주 활용할 예정이라 속성을 만들어 둔다.
        self.head=self.snake_shape[0]


    def create_snake(self):
        for position in STARTING_POSITIONS:
            seq = Turtle("square")
            seq.color('white')
            seq.penup()
            seq.goto(position)
            self.snake_shape.append(seq)

    def move(self):
        for num in range(len(self.snake_shape) - 1, 0, -1):
            new_x = self.snake_shape[num - 1].xcor()
            new_y = self.snake_shape[num - 1].ycor()
            self.snake_shape[num].goto(new_x, new_y)
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

