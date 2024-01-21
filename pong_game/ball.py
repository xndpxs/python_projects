from turtle import Turtle

MOVE_SPEED = 0.1


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("black")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = MOVE_SPEED

    def set_position(self, position):
        self.penup()
        self.goto(position, 0)

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1
        # Establece un límite máximo para la velocidad
        max_speed = 0.02  # Ajusta este valor según sea necesario

        # Solo aumenta la velocidad si aún no ha alcanzado el máximo
        if self.move_speed > max_speed:
            self.move_speed *= 0.9

    def bounce_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = MOVE_SPEED
        self.bounce_x()
