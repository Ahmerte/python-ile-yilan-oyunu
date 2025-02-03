import random
import turtle
import time

# Oyun Hızı
DELAY = 0.15

# Pencere Ayarları
pencere = turtle.Screen()
pencere.title('Yılan Oyunu')
pencere.bgcolor('lightgreen')
pencere.setup(width=600, height=600)
pencere.tracer(0)

# Yılan Baş
kafa = turtle.Turtle()
kafa.shape("square")
kafa.color("black")
kafa.penup()
kafa.goto(0, 100)
kafa.direction = "stop"

# Yemek
yemek = turtle.Turtle()
yemek.shape("circle")
yemek.color("red")
yemek.penup()
yemek.shapesize(0.80, 0.80)
yemek.goto(0, 0)

# Kuyruk Listesi ve Puan
kuyruklar = []
puan = 0

yaz = turtle.Turtle()
yaz.speed(0)
yaz.color("white")
yaz.penup()
yaz.hideturtle()
yaz.goto(0, 260)
yaz.write(f"Puan: {puan}", align="center", font=("Courier", 24, "normal"))

# Hareket Fonksiyonu
def move():
    x, y = kafa.xcor(), kafa.ycor()
    if kafa.direction == "up":
        kafa.sety(y + 20)
    elif kafa.direction == "down":
        kafa.sety(y - 20)
    elif kafa.direction == "right":
        kafa.setx(x + 20)
    elif kafa.direction == "left":
        kafa.setx(x - 20)

# Yönlendirme Fonksiyonları
def go_up():
    if kafa.direction != "down":
        kafa.direction = "up"

def go_down():
    if kafa.direction != "up":
        kafa.direction = "down"

def go_right():
    if kafa.direction != "left":
        kafa.direction = "right"

def go_left():
    if kafa.direction != "right":
        kafa.direction = "left"

# Klavye Kontrolleri
pencere.listen()
pencere.onkey(go_up, "Up")
pencere.onkey(go_down, "Down")
pencere.onkey(go_right, "Right")
pencere.onkey(go_left, "Left")

# Oyun Döngüsü
while True:
    pencere.update()

    # Kenarlara Çarpma Kontrolü
    if abs(kafa.xcor()) > 290 or abs(kafa.ycor()) > 290:
        time.sleep(1)
        kafa.goto(0, 0)
        kafa.direction = "stop"
        for kuyruk in kuyruklar:
            kuyruk.goto(1000, 1000)
        kuyruklar.clear()
        puan = 0
        yaz.clear()
        yaz.write(f"Puan: {puan}", align="center", font=("Courier", 24, "normal"))
        DELAY = 0.15

    # Yemek Yendiğinde
    if kafa.distance(yemek) < 20:
        yemek.goto(random.randint(-250, 250), random.randint(-250, 250))
        yeni_kuyruk = turtle.Turtle()
        yeni_kuyruk.shape("square")
        yeni_kuyruk.color("white")
        yeni_kuyruk.penup()
        kuyruklar.append(yeni_kuyruk)
        puan += 10
        yaz.clear()
        yaz.write(f"Puan: {puan}", align="center", font=("Courier", 24, "normal"))
        DELAY = max(0.05, DELAY - 0.002)

    # Kuyruk Hareketi
    for i in range(len(kuyruklar) - 1, 0, -1):
        kuyruklar[i].goto(kuyruklar[i - 1].pos())
    if kuyruklar:
        kuyruklar[0].goto(kafa.pos())

    move()

    # Yılanın Kendine Çarpma Kontrolü
    for segment in kuyruklar:
        if segment.distance(kafa) < 20:
            time.sleep(1)
            kafa.goto(0, 0)
            kafa.direction = "stop"
            for segment in kuyruklar:
                segment.goto(1000, 1000)
            kuyruklar.clear()
            puan = 0
            yaz.clear()
            yaz.write(f"Puan: {puan}", align="center", font=("Courier", 24, "normal"))
            DELAY = 0.15

    time.sleep(DELAY)
