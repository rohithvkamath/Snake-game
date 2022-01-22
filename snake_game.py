from tkinter import *
import turtle
import random
ws=tr=Tk()                                      
def start():
    ws.destroy()            # Closes the Start window and goes for Snake Game.
    w = 1000                # Setting constant width for the screen.
    h = 700                 # Setting constant height for the screen.
    fs = 10                 
    d = 100                 # Speed of the movement of snake in milliseconds

    offsets = {                     # defines by how much offset the snake should turn.
        "up": (0, 20),                 
        "down": (0, -20),
        "left": (-20, 0),
        "right": (20, 0)
    }

    def main():
        
        global snake, head, snake_food1, pen
        snake = [[0, 0], [0, 20], [0, 40], [0, 60], [0, 80]]            # initial distance between the snake body parts.
        head = "up"                                                     # initial position of the head is set to up.
        snake_food1 = position()                                             # Function call to return random co-ordinates for the food.
        food.goto(snake_food1)                                          # placing the food in defined cordinates.
        condition()                                                     # Checks the condition of the snake. 
        
    
    def condition():                                                    # Checks the condition of the Snake.
        global head
        new_head = snake[-1].copy()                                     # Creates a copy of tail of the snake
        new_head[0] = snake[-1][0] + offsets[head][0]
        new_head[1] = snake[-1][1] + offsets[head][1]
        if new_head in snake[:-1]:                                      # Checks if the snake bits itself.
            tr=Tk()                                                     # If it bits itself, a window is opened with options.
            tr.title("Snake Game")
            tr.geometry('200x200')
            Button(tr, text="Try Again", command=main ).pack()                      
            Button(tr,text="Close window",command=tr.destroy).pack()
            Button(tr, text="Exit", command=exit).pack()
            tr.mainloop()        
        else:                                                           # If it doesn't bite itself,then
            snake.append(new_head)                                      # adds new head.
            if not snake_food():                             
                snake.pop(0) 

            if snake[-1][0] > w / 2:                                    # These conditions are if the snake goes out of screen.
                snake[-1][0] -= w
            elif snake[-1][0] < - w / 2:
                snake[-1][0] += w
            elif snake[-1][1] > h / 2:
                snake[-1][1] -= h
            elif snake[-1][1] < -h / 2:
                snake[-1][1] += h

            pen.clearstamps()                       # clears all the stamps
            
            for segment in snake:
                pen.goto(segment[0], segment[1])
                pen.stamp()

            screen.update()                         # updates the turtle.screen screen
 
            turtle.ontimer(condition, d)

    def snake_food():                                       # Places the food at random position.
        global snake_food1
        if dist(snake[-1], snake_food1) < 20:               # this condition checks if the snake has eaten the food.
            snake_food1 = position()
            food.goto(snake_food1)
            return True
        return False

    def position():                                             # gives a random position.
        x = random.randint(- w / 2 + fs, w / 2 - fs)
        y = random.randint(- h / 2 + fs, h / 2 - fs)
        return (x, y)

    def dist(pos1, pos2):                                       # gives the distance between snake and food.
        x1, y1 = pos1
        x2, y2 = pos2
        distance = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5
        return distance
    # The below function defines how the response should be for the input arrow keys.
    def go_up():
        global head
        if head != "down":
            head = "up"

    def go_right():
        global head
        if head != "left":
            head = "right"

    def go_down():
        global head
        if head != "up":
            head = "down"

    def go_left():
        global head
        if head != "right":
            head = "left"
    # The below codes are the necessary functions to create amd run the screen.
    screen = turtle.Screen()
    screen.setup(w, h)
    screen.title("Snake Game")
    screen.bgcolor("black")
    screen.setup(1000, 750)
    screen.tracer(0)
    
    pen = turtle.Turtle("square")
    pen.shape("circle")
    pen.color("red")
    pen.penup()

    food = turtle.Turtle()
    food.shape("circle")
    food.color("blue")
    food.shapesize(fs /8) 
    food.penup()

    screen.listen()
    screen.onkeypress(go_up, "Up")
    screen.onkeypress(go_right, "Right")
    screen.onkeypress(go_down, "Down")
    screen.onkeypress(go_left, "Left")

    main()                  # Calling the function initially.
    turtle.done()           # Creating a turtle loop

def init():                                 # This code is the initial pop up window.
    ws.title("Snake Game")
    ws.geometry('700x700')
    photo1=PhotoImage(file="buttons/start.png")
    photo2=PhotoImage(file="buttons/exit.png")
    Button1 = Button(ws, image=photo1, command=start,borderwidth=0).pack(pady=10)
    Button2 = Button(ws, image=photo2, command=exit,borderwidth=0).pack(pady=10)
    ws.mainloop()
init() 