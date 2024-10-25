import turtle
import random as rand

spot_colors = ["red", "green", "blue", "yellow", "purple", "orange"]
spot_sizes = [0.75, 1, 1.5, 2]
score = 0
timer = 30
timer_up = False


wn = turtle.Screen()
wn.bgcolor("black")


spot = turtle.Turtle()
spot.shape("circle")
spot.penup()
spot.hideturtle()  # hide initially

score_writer = turtle.Turtle()
score_writer.hideturtle()
score_writer.penup()
score_writer.goto(0, 250)
score_writer.color("white")

counter_writer = turtle.Turtle()
counter_writer.hideturtle()
counter_writer.penup()
counter_writer.goto(0, -250)
counter_writer.color("white")

# Start the game
def start_game():
    global score, timer_up
    score = 0
    timer_up = False
    update_score()
    countdown()
    change_position()
    spot.showturtle()

def update_score():
    score_writer.clear()
    score_writer.write(f"Score: {score}", font=("Arial", 20, "normal"))

def change_position():
    spot.fillcolor(rand.choice(spot_colors))
    spot.stamp()  # leave a stamp
    spot.shapesize(rand.choice(spot_sizes))
    spot.goto(rand.randint(-190, 190), rand.randint(-140, 140))

def spot_clicked(x, y):
    global score
    if not timer_up:
        score += 1
        update_score()
        change_position()

def countdown():
    global timer
    global timer_up
    if timer > 0:
        timer -= 1
        counter_writer.clear()
        counter_writer.write(f"Time left: {timer}s", font=("Arial", 20, "normal"))
        wn.ontimer(countdown, 1000)
    else:
        timer_up = True
        spot.hideturtle()
        counter_writer.write("Time's up!", font=("Arial", 20, "normal"))

spot.onclick(spot_clicked)
start_game()
wn.mainloop()
