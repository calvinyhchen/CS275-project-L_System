import turtle

def applyRules(axiom, rules, nIter):
    prev = axiom
    for i in range(nIter):
        finalString = ""
        for j in range(len(prev)):
            if prev[j] == '[' or prev[j] == ']':
                finalString += prev[j]
                continue
            finalString +=  rules[prev[j]]
        prev = finalString
        if i == nIter-1:
            return finalString

        
def def_Alphabet(alphabet):
    interpts = {}
    for alpha in alphabet:
        inter = raw_input("interpretation for %s: <action, degree>: " % alpha)
        if "forward" in inter.split()[0]:
            act = 'f'
        elif "backward" in inter.split()[0]:
            act = 'b'
        elif "right" in inter.split()[0]:
            act = 'r'
        elif "left" in inter.split()[0]:
            act = 'l'
        else:
            print("input error")
            break

        degree = float(inter.split()[1])
        interpts[alpha] = (act, degree)
    interpts['['] = ('[',0)
    interpts[']'] = (']',0)
    return interpts


def drawLsystem(myTurtle, finalString, interpts):
    turtleStackPos = []
    turtleStackAng = []
    for i in range(len(finalString)):
        if interpts[finalString[i]][0] == 'f':
            myTurtle.forward(interpts[finalString[i]][1])
        elif interpts[finalString[i]][0] == 'b':
            myTurtle.backward(interpts[finalString[i]][1])
        elif interpts[finalString[i]][0] == 'r':
            myTurtle.right(interpts[finalString[i]][1])
        elif interpts[finalString[i]][0] == 'l':
            myTurtle.left(interpts[finalString[i]][1])
        elif interpts[finalString[i]][0] == '[':
            turtleStackPos.append(myTurtle.pos())
            turtleStackAng.append(myTurtle.heading())
        elif interpts[finalString[i]][0] == ']':
            curPos = turtleStackPos.pop()
            curAng = turtleStackAng.pop()
            myTurtle.penup()
            myTurtle.setpos(curPos)
            myTurtle.setheading(curAng)
            myTurtle.pendown()




def initTurtle():
    myTurtle = turtle.Turtle()
    scrTurtle = turtle.Screen()
  

    init_x = input("initial position x: ")  
    init_y = input("initial position y: ")  
    init_angle = input("initial angle: ")

    myTurtle.penup()
    myTurtle.setx(init_x)
    myTurtle.sety(init_y)
    myTurtle.setheading(init_angle)
    myTurtle.pendown()
    myTurtle.speed(10000)
    
    return myTurtle,scrTurtle

def initPara():
    alphabet_count = input("how many alphabet: ")
    
    alphabet = []
    for i in range(alphabet_count):
        temp_alpha = raw_input("alphabet %s: " % str(i+1))
        alphabet.append(temp_alpha) 
    
    axiom = raw_input("axiom: ")
    
    rules = {}
    for i in range(alphabet_count):
        temp_rule = raw_input("rule for %s: " % alphabet[i])
        rules[alphabet[i]] = temp_rule
    
    interpts = def_Alphabet(alphabet)
    nIter = input("how many iterations: ")

    return alphabet, axiom, rules, interpts, nIter

if __name__ == "__main__":
    alphabet, axiom, rules, interpts, nIter = initPara()

    finalString = applyRules(axiom,rules,nIter)

    myTurtle, scrTurtle = initTurtle()

    drawLsystem(myTurtle,finalString, interpts)
    
    scrTurtle.exitonclick()
