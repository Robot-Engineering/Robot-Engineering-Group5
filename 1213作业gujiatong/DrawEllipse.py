import turtle
import math

class DrawEllipse:
    def __init__(self,x,y,a,b):
        self.x=0
        self.y=0
        self.a=a
        self.b=b

    def ellipse(self,x,y,a,b):
        turtle.tracer(False)
        turtle.setup(800, 800)
        turtle.pencolor('black')
        turtle.speed(0)
        turtle.pensize(1)
        turtle.penup()
        turtle.setpos(x+a, 0)  # 初始点的位置
        turtle.pendown()
        turtle.hideturtle()
        for i in range(1000):
            radian = 2 * math.pi / 1000  
            x = radian * (i + 1)  # 每次弧度增加radian
            next_point = (a * math.cos(x), b * math.sin(x))
            turtle.setpos(next_point)
        turtle.mainloop()

    def show(self):
        DrawEllipse.ellipse(drawellipse,self.x,self.y,self.a,self.b)
        print(self.x,self.y)

a=int(input("输入椭圆的长半轴："))
b=int(input("输入椭圆的短半轴："))
x=0
y=0
drawellipse=DrawEllipse(x,y,a,b)
DrawEllipse.show(drawellipse)