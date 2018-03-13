import turtle

r1 = 0.75
r2 = 0.77
a1 = 35
a2 = -35
psi1 = 0
psi2 = 0
w0 = 30
q = 0.5
e = 0.4
minValue = 0.0
nIter = 2
axiom = "A(100,30)"

def A(s, w, n, finalString):
    if n == nIter or s < minValue:
        return finalString
    new_s1 = s*r1
    new_w1 = w*(q**e)
    new_s2 = s*r2
    new_w2 = w*((1-q)**e)
    finalString = '!(%.2f)F(%.2f)[+(%.2f)/(%.2f)%s][+(%.2f)/(%.2f)%s]' % (w, s, a1, psi1, A(new_s1, new_w1, n+1,""), a2, psi2, A(new_s2, new_w2, n+1,""))
    return finalString

def parse_paren(string):
    stack = []
    a1 = 0.0
    a2 = 0.0
    i = 0
    for i, c in enumerate(string):
        if c == '(':
            stack.append(i)
        elif c == ',':
            start = stack.pop()
            a1 = float(string[start+1:i])
            stack.append(i)
        elif c == ')':
            start = stack.pop()
            a2 = float(string[start+1:i])
            break
    return a1, a2, i

def drawLsystem(myTurtle, finalString):
    turtleStackPos = []
    turtleStackAng = []
    i = 0
    while i < len(finalString):
        step = 0
        if finalString[i] == 'A':
            continue
        elif finalString[i] == '!':        
            t1, t2, step = parse_paren(finalString[i+1:])
            myTurtle.width(t2)
        elif finalString[i] == 'F':        
            t1, t2, step = parse_paren(finalString[i+1:])
            myTurtle.forward(t2)
        elif finalString[i] == '+':        
            t1, t2, step = parse_paren(finalString[i+1:])
            myTurtle.left(t2)
        elif finalString[i] == '/':        
            t1, t2, step = parse_paren(finalString[i+1:])
            myTurtle.tilt(t2)
        elif finalString[i] == '[':
            turtleStackPos.append(myTurtle.pos())
            turtleStackAng.append(myTurtle.heading())
        elif finalString[i] == ']':
            curPos = turtleStackPos.pop()
            curAng = turtleStackAng.pop()
            myTurtle.penup()
            myTurtle.setpos(curPos)
            myTurtle.setheading(curAng)
            myTurtle.pendown()
        i = i+step+1;


def initTurtle():
    myTurtle = turtle.Turtle()
    scrTurtle = turtle.Screen()
  
    init_x = 0
    init_y = -300
    init_angle = 90

    myTurtle.penup()
    myTurtle.setx(init_x)
    myTurtle.sety(init_y)
    myTurtle.setheading(init_angle)
    myTurtle.pendown()
    myTurtle.speed(5)
    
    return myTurtle,scrTurtle


if __name__ == "__main__":

    finalString = A(100,30,0,"")
    print(finalString)
    myTurtle, scrTurtle = initTurtle()

    drawLsystem(myTurtle,finalString)
    
    scrTurtle.exitonclick()
