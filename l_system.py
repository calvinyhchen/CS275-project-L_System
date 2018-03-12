import turtle

def applyRules(alphabet, axiom, rules, nIter):
    prev = axiom
    finalString = ""
    for i in range(nIter):
        for j in range(len(prev)):
            finalString +=  rules[prev[j]]
        print(finalString)
        prev = finalString
        finalString = ""
        
    return finalString

def drawLsystem(myTurtle, finalString):
    for alpha in finalString:
        if alpha == 'a':
            myTurtle.forward(10)
        elif alpha == 'b':
            myTurtle.backward(10)
        elif alpha == '+':
            myTurtle.right(60)
        elif alpha == '-':
            myTurtle.left(60)


def initTurtle(finalString):
    myTurtle = turtle.Turtle()
    scrTurtle = turtle.Screen()
  

    myTurtle.speed(5)
    
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
    
    nIter = input("how many iterations: ")

    return alphabet, axiom, rules, nIter

if __name__ == "__main__":
    alphabet, axiom, rules, nIter = initPara()

    finalString = applyRules(alphabet,axiom,rules,nIter)

    myTurtle, scrTurtle = initTurtle(finalString)

    drawLsystem(myTurtle,finalString)
    
    scrTurtle.exitonclick()
