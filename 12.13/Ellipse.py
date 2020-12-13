import turtle as t
import math


class Ellipse:
    def __init__(self,x,y,a,b):
        self.x=x
        self.y=y
        self.a=a
        self.b=b

    def set(self,X,Y,A,B):
        self.x=X
        self.y=Y
        self.a=A
        self.b=B

    def show(self):
        t.tracer(False)
        t.pensize(2)
        t.penup()
        t.goto(self.x,self.y)
        t.setpos(self.a,0)
        t.pendown()
        t.hideturtle()
        for i in range(10000):
            radian= 2 * math.pi / 10000
            x= radian * (i+1)
            next_point= (self.a * math.cos(x),self.b * math.sin(x))
            t.setpos(next_point)
        t.mainloop()
        
