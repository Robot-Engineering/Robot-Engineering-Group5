import turtle as t


class Polygon:
    def __init__(self,x,y,n,length):
        self.x=x
        self.y=y
        self.n=n
        self.length=length

    def set(self,X,Y,N,Length):
        self.x=X
        self.y=Y
        self.n=N
        self.length=Length

    def show(self):
        t.tracer(False)
        t.pensize(2)
        t.penup()
        t.goto(self.x,self.y)
        t.pendown()
        for _ in range(0,self.n):
            t.fd(self.length)
            t.rt(180-180*(self.n-2)/self.n)
