import turtle


def main():
    t = turtle.Turtle()
    t.speed(0)

    

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


if __name__ == "__main__":
    main()