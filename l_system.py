import turtle

def applyRules(alphabet, axiom, rules, nIter):
    prev = axiom
    finalString = ""
    for i in range(nIter):
        for j in range(len(prev)):
            finalString +=  rules[prev[j]]
        prev = finalString
        if i == nIter-1:
            return finalString
        finalString = ""
        

def drawLsystem(myTurtle, finalString):
    for alpha in range(len(finalString)):
        if finalString[alpha] == 'F':
            print(finalString[alpha])
            myTurtle.forward(10)
        elif finalString[alpha] == 'B':
            myTurtle.backward(10)
        elif finalString[alpha] == '+':
            myTurtle.right(60)
        elif finalString[alpha] == '-':
            myTurtle.left(60)


def initTurtle():
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

    myTurtle, scrTurtle = initTurtle()

    drawLsystem(myTurtle,finalString)
    
    scrTurtle.exitonclick()
