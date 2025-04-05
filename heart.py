import turtle
import math

def xt(t):
    return 16 * math.sin(t) ** 3

def yt(t):
    return 13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t)

try:
    t = turtle.Turtle()
    t.speed(500)
    turtle.colormode(255)
    turtle.Screen().bgcolor(0, 0, 0)

    # Добавляем текст сразу перед началом рисования
    t.penup()
    t.goto(0, -340)
    t.pendown()
    t.color("white")
    t.write("°.• For:  •                                            • From: •.°", align="center", font=("Arial", 16, "normal"))

    #  Рисуем фигуру
    for i in range(2550):
        t.goto(xt(i) * 20, yt(i) * 20)
        t.pencolor(255 - i % 255, i % 255, (255 + i) // 2 % 255)
        t.goto(0, 0)

    t.hideturtle()
    turtle.update()
    turtle.mainloop()

except turtle.Terminator:
    # Обработка закрытия окна
    print("Окно закрыто.")
