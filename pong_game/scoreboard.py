from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Fira Sans", 60, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.pensize(10)
        # Dibuja la línea entrecortada en el centro
        self.penup()  # Levanta el lápiz para no dibujar mientras se mueve
        self.goto(0, -300)  # Posición inicial en la parte inferior de la pantalla
        self.setheading(90)  # Dirección hacia arriba

        for _ in range(16):  # Número de segmentos
            self.pendown()  # Baja el lápiz para comenzar a dibujar
            self.forward(20)  # Dibuja un segmento
            self.penup()  # Levanta el lápiz para dejar un espacio
            self.forward(20)  # Espacio entre segmentos

        # Actualiza los marcadores
        self.goto(-100, 200)
        self.write(f"{self.l_score}", align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(f"{self.r_score}", align=ALIGNMENT, font=FONT)

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()
