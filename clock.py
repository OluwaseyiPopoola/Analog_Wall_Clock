import turtle


def main():
    t = turtle.Turtle()
    

def write_numbers(t: turtle.Turtle):
    w = turtle.Screen().window_width()
    h = turtle.Screen().window_height()
    min_dim = min(w, h)
    radius = (min_dim // 2) * 0.6
    font_size = min_dim // 25

    t.penup()
    t.setheading(60)  # Start pointing up

    for i in range(1, 13):
        t.forward(radius - font_size)
        t.write(f"{i}", align="center", font=("Arial", font_size, "normal"))
        t.backward(radius - font_size)
        t.right(30)  # Move to next hour

    t.setheading(90)


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