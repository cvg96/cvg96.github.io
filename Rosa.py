import turtle
import math

# Configuración inicial de Turtle
turtle.speed(2)
turtle.bgcolor("lightgreen")
turtle.pensize(2)
turtle.hideturtle()

# Función para dibujar un pétalo de la rosa
def draw_petal(radius, angle):
    turtle.circle(radius, angle)
    turtle.left(180 - angle)
    turtle.circle(radius, angle)
    turtle.left(180 - angle)

# Función para dibujar una rosa con varios pétalos
def draw_rose(num_petals, petal_size):
    for _ in range(num_petals):
        draw_petal(petal_size, 60)
        turtle.left(360 / num_petals)

# Función principal para dibujar una rosa completa
def draw_complete_rose():
    turtle.color("red")
    draw_rose(6, 100)  # Puedes ajustar el número de pétalos y el tamaño

    # Dibuja el tallo
    turtle.color("green")
    turtle.right(90)
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(20)

    # Cierra la ventana al hacer clic
    turtle.exitonclick()

# Llama a la función principal
draw_complete_rose()