import turtle
from datetime import datetime


def main():
    t = turtle.Turtle()
    t.speed(0)
    draw_clock_frame(t)
    write_numbers(t)

    time_now = datetime.now()

     
    draw_second_hand(t, time_now)
    draw_minute_hand(t, time_now)
    draw_hour_hand(t, time_now)
    turtle.done()
    
    
def draw_second_hand(t: turtle.Turtle, time_now: datetime):
    w = turtle.Screen().window_width()
    h = turtle.Screen().window_height()
    min_dim = min(w, h)
    radius = (min_dim // 2) * 0.5

    second = time_now.second
    angle_turned = (360 / (60)) * second
    
    t.pensize(5)
    t.right(angle_turned)
    t.forward(radius)
    t.backward(radius)
    t.setheading(90)

def draw_minute_hand(t: turtle.Turtle, time_now: datetime):
    w = turtle.Screen().window_width()
    h = turtle.Screen().window_height()
    min_dim = min(w, h)
    radius = (min_dim // 2) * 0.4

    minute = time_now.minute 
    angle_turned = (360 / (60)) * minute
    
    t.pensize(6)
    t.right(angle_turned)
    t.forward(radius)
    t.backward(radius)
    t.setheading(90)

def draw_hour_hand(t: turtle.Turtle, time_now: datetime):
    w = turtle.Screen().window_width()
    h = turtle.Screen().window_height()
    min_dim = min(w, h)
    radius = (min_dim // 2) * 0.2

    hour = time_now.hour + (time_now.minute / 60)
    angle_turned = (360 / 12) * hour
    
    t.pensize(9)
    t.right(angle_turned)
    t.forward(radius)
    t.backward(radius)
    t.setheading(90)




def write_numbers(t: turtle.Turtle):
    w = turtle.Screen().window_width()
    h = turtle.Screen().window_height()
    min_dim = min(w, h)
    radius = (min_dim // 2) * 0.6
    font_size = min_dim // 25

    t.penup()
    t.setheading(90)  # Start pointing up

    for i in range(1, 13):
        t.forward(radius - font_size)
        t.write(f"{i}", align="center", font=("Arial", font_size, "normal"))
        t.backward(radius - font_size)
        t.right(30)  # Move to next hour

    t.pendown()

def draw_clock_frame(t: turtle.Turtle): 
    """Draws the outer clock frame"""
    draw_circle(t, 0.80)
    draw_circle(t, 0.70)

def draw_circle(t: turtle.Turtle, scale: int):
    
    w = turtle.Screen().window_width()
    h = turtle.Screen().window_height()

    min_dim = min(w, h)
    radius = scale*(min_dim // 2) 

    t.penup()
    t.goto(0, -radius) 
    t.pendown()

    t.circle(radius) # draws circle

    # returning t to initial position
    t.penup()
    t.goto(0,0)
    t.setheading(0)


if __name__ == "__main__":
    main()