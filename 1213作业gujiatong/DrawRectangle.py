import turtle

class DrawRectangle:
    def __init__(self,x,y,width,height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height

    def rectangle(self,x,y,width,height):
        turtle.tracer(False)
        turtle.setup(800, 800)
        turtle.pencolor('black')
        turtle.speed(0)
        turtle.pensize(1)
        turtle.penup()
        turtle.goto(self.x,self.y)
        turtle.pendown()
        turtle.hideturtle()
        turtle.left(90)
        turtle.forward(self.width)
        turtle.right(90)
        turtle.forward(self.height)
        turtle.right(90)
        turtle.forward(self.width)
        turtle.right(90)
        turtle.forward(self.height)
        done()

    def show(self):
        DrawRectangle.rectangle(drawrectangle,self.x,self.y,self.width,self.width)
        print(self.x,self.y)
        
width=int(input("输入矩形的宽："))
height=int(input("输入矩形的长："))
x=0
y=0
drawrectangle=DrawRectangle(x,y,width,height)
DrawRectangle.show(drawrectangle)