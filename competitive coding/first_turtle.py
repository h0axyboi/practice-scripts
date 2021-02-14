import turtle
screen=turtle.Screen()
screen.bgcolor("lightgreen")

dimx=22*30; dimy=22*30; screen.setup(dimx,dimy)
shift=[-dimx/2,-dimy/2]

sprite=turtle.Turtle()
sprite.shape('square')
sprite.penup()
sprite.speed(0)
sprite.goto(-1000,1000)

running=False
def update():
    global running
    if running:
        move()
        screen.ontimer(update,350)

def startgame():
    global running
    running=True
    create_body(dimx/2+shift[0],dimy/2+shift[1])
    update()

snake=[]
def create_body(x,y):
    body=sprite.clone()
    body.goto(x,y)
    snake.append(body)

dir="Right"
def move():
    last=snake[-1]
    first=snake[0]
    x=first.xcor()
    y=first.ycor()
    size=22
    if dir=='Right':
        last.goto(((x+size-shift[0])%dimx)+shift[0],y)
    elif dir=='Left':
        last.goto(((x-size-shift[0])%dimx)+shift[0],y)
    elif dir=='Up':
        last.goto(x,((y+size-shift[1])%dimy)+shift[1])
    elif dir=='Down':
        last.goto(x,((y-size-shift[1])%dimy)+shift[1])
    snake.insert(0,last)
    snake.pop()

def up():
    global dir
    if not dir=='Down':
        dir='Up'
def down():
    global dir
    if not dir=='Up':
        dir='Down'
def right():
    global dir
    if not dir=='Left':
        dir='Right'
def left():
    global dir
    if not dir=='Right':
        dir='Left'

screen.onkey(up,'Up')
screen.onkey(down,'Down')
screen.onkey(right,'Right')
screen.onkey(left,'Left')
screen.listen()

startgame()

turtle.mainloop()
