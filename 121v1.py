# Import statements
import turtle
import random as rand

# Game configuration
spot_color = "pink"
spot_size = 2
spot_shape = "circle"
score = 0
font_setup = ("Arial", 20, "normal")
timer = 30
counter_interval = 1000  # 1000 represents 1 second
timer_up = False

# Initialize turtle objects
spot = turtle.Turtle()
spot.shape(spot_shape)
spot.shapesize(spot_size)
spot.fillcolor(spot_color)
spot.penup()

# Score writer turtle
score_writer = turtle.Turtle()
score_writer.hideturtle()
score_writer.penup()
score_writer.goto(-200, 200)

# Countdown timer writer turtle
counter = turtle.Turtle()
counter.hideturtle()
counter.penup()
counter.goto(200, 200)

# Game functions
def spot_clicked(x, y):
    """Handles the event when the turtle is clicked."""
    global timer_up
    if not timer_up:
        update_score()
        change_position()
    else:
        spot.hideturtle()

def change_position():
    """Moves the turtle to a new random location."""
    new_xpos = rand.randint(-200, 200)
    new_ypos = rand.randint(-200, 200)
    spot.goto(new_xpos, new_ypos)

def update_score():
    """Updates the score each time the turtle is clicked."""
    global score
    score += 1
    score_writer.clear()
    score_writer.write(f"Score: {score}", font=font_setup)

def countdown():
    """Handles the countdown timer."""
    global timer, timer_up
    counter.clear()
    if timer <= 0:
        counter.write("Time's up!", font=font_setup)
        timer_up = True
    else:
        counter.write(f"Timer: {timer}", font=font_setup)
        timer -= 1
        turtle.ontimer(countdown, counter_interval)

# Events
wn = turtle.Screen()
wn.bgcolor("lightblue")

spot.onclick(spot_clicked)

# Start the timer and the game loop
countdown()

wn.mainloop()
