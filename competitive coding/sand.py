import turtle
screen=turtle.Screen()
screen.bgcolor("lightgreen")
dimx=800; dimy=500; screen.setup(dimx,dimy)
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

dir='Right'
def move():
    first=snake[0]
    last=snake[-1]


snake=[]
def create_body(x,y):
    body=sprite.clone()
    body.goto(x,y)
    snake.append(body)

startgame()
turtle.mainloop()
