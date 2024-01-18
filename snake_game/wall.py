from turtle import Turtle

WALL_SIZE = 290
WALL_TIHCKNESS = 10


class Wall(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.pensize(WALL_TIHCKNESS)
        self.color("black")
        self.draw_walls()

    def draw_walls(self):
        for _ in range(4):
            self.goto(-WALL_SIZE, WALL_SIZE)
            self.pendown()
            self.goto(WALL_SIZE, WALL_SIZE)
            self.goto(WALL_SIZE, -WALL_SIZE)
            self.goto(-WALL_SIZE, -WALL_SIZE)
            self.goto(-WALL_SIZE, WALL_SIZE)
            self.penup()

    def detect_collision_wall(self, snake, scoreboard):
        if (
            snake.head.xcor() > WALL_SIZE
            or snake.head.xcor() < -WALL_SIZE
            or snake.head.ycor() > WALL_SIZE
            or snake.head.ycor() < -WALL_SIZE
        ):
            return True
        return False
