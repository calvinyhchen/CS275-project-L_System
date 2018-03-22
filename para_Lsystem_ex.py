import turtle
import math
import numpy as np

# A(100, 30)
# A(s, w):s>=0 ->!(w)F(s)[+(35)/(0)A(s*0.75, w*(0.5)^(0.4)))][+(-35)/(0)A(s*0.77, w*(0.5)^(0.4))]

def initTurtle():
    myTurtle = turtle.Turtle()
    scrTurtle = turtle.Screen()
  

    # init_x = input("initial position x: ")  
    # init_y = input("initial position y: ")  
    # init_angle = input("initial angle: ")
    init_x = 0
    init_y = -50
    init_angle = 90

    myTurtle.penup()
    myTurtle.setx(init_x)
    myTurtle.sety(init_y)
    myTurtle.setheading(init_angle)
    myTurtle.pendown()
    myTurtle.speed(5)
    
    return myTurtle,scrTurtle

def get_content(string):
    p = string.find('(')
    q = string.find(')')
    return string[:p], string[p+1:q], string[min(q+1, len(string)-1):]


def intrp_cond(cond):
    b = cond.find('>')
    left = b
    s = cond.find('<')
    if s != -1 and s < b:
        left = s
    e = cond.find('=')
    if e != -1 and e < b:
        left = e
    right = max(b,s,e)
    return [ cond[:left], cond[left:right+1], cond[right+1:] ]

def intrp_expr(expr):
# A(s, w):s>=0 -> !(w)F(s)[()+(35)/(0)A(s*0.75, w*0.5^0.4)]()[()+(-35)/(0)A(s*0.77, w*0.5^0.4)]()
# !, w, F, s, [, , +, 35, / 0, A, (s*0.75, w*(0.5)^(0.4)), ], , [, , +, -35, /, 0, A, (s*0.77, w*(0.5)^(0.4)), ], 
    
    action_list = []
    expr_list = expr.split(')')
    for ep in expr_list:
        if ep != '':
            f = ep[0]
            p = ep[ep.find('(')+1:]
            action_list.append((f, p))
    return action_list


def parse(string):
    func, cond_expr = string.split(':')
    func_name, paras, _ = get_content(func)
    cond, expr = cond_expr.split('->')

    cond = intrp_cond(cond.strip())
    expr = intrp_expr(expr.strip())
    return func_name, paras, cond, expr
    
    
def check(func_paras, func_cond, paras):
    cond = ""
    for c in func_cond:
        if c in func_paras.split(','):
            indx = func_paras.index(c)
            cond += paras.split(',')[indx]
        else:
            cond += c
    print cond, eval(cond)
    return eval(cond)


def apply_para(func_paras, func_expr, paras):
    applied_expr = []
    for (child_func, child_paras) in func_expr:
        if child_paras == '':
            applied_expr.append((child_func, child_paras))
        else:
            if ',' in child_paras:
                child_paras = child_paras.split(',')
            else:
                child_paras = [child_paras]
            applied_child_paras = []
            for fp in child_paras:
                new_fp = ''
                for c in fp:
                    # print c, func_paras.split(','), paras.split(',')
                    if c in func_paras.split(','):
                        indx = func_paras.split(',').index(c)
                        new_fp += paras.split(',')[indx]
                    else:
                        new_fp += c
                applied_child_paras.append(str(eval(new_fp)))
            applied_child_paras = ','.join(applied_child_paras)
            applied_expr.append((child_func, applied_child_paras))
    print 'applied',applied_expr
    return applied_expr

def unfold(action_list, functions, n):
    all_actions = []
    all_actions.extend(action_list)
    for i in range(n):
        print 'i', i
        print all_actions
        new_actions = []
        for (func, paras) in all_actions:
            if func in functions:
                if check(functions[func][0], functions[func][1], paras):
                    print func, '(', functions[func][0], ') use (' , paras, ')'
                    new_actions.extend(apply_para(functions[func][0], functions[func][2], paras))
            else:
                new_actions.append((func, paras))
        all_actions = new_actions
    return all_actions

def rotate(H,L,U,R):
    M = np.array([H,L,U]) 
    M = np.matmul(R,M)
    H = M[0]
    L = M[1]
    U = M[2]
    return H,L,U

def execute(all_actions):
    myTurtle, scrTurtle = initTurtle()
    turtleStackPos = []
    direction_stack = []
    H = [1,0,0]
    L = [0,1,0]
    U = [0,0,1]
    initial = myTurtle.heading()
    for (func, para) in all_actions:
        if func == '!': # set width
            myTurtle.width(float(para))
        elif func == '/': # tilt left
            thetaH = (float(para)/180)*math.pi
            R = []
            R.append([1,0,0])
            R.append([0,math.cos(thetaH),-math.sin(thetaH)])
            R.append([0,math.sin(thetaH),math.cos(thetaH)])
            H,L,U = rotate(H,L,U,R)
            head = math.atan(H[1]/H[0])*180/math.pi
            myTurtle.setheading(initial+head)
        elif func == '+':
            thetaH = (float(para)/180)*math.pi
            R = []
            R.append([math.cos(thetaH),math.sin(thetaH),0])
            R.append([-math.sin(thetaH),math.cos(thetaH),0])
            R.append([0,0,1])
            H,L,U = rotate(H,L,U,R)
            head = math.atan(H[1]/H[0])*180/math.pi
            myTurtle.setheading(initial+head)
        elif func == '-':
            myTurtle.right(float(para))
        elif func == 'F':
            myTurtle.forward(float(para)*math.cos(H[2]))
        elif func == '[':
            turtleStackPos.append(myTurtle.pos())
            direction_stack.append([H,L,U])
        elif func == ']':
            curPos = turtleStackPos.pop()
            D = direction_stack.pop()
            H = D[0]
            L = D[1]
            U = D[2]
            myTurtle.penup()
            myTurtle.setpos(curPos)
            head = math.atan(H[1]/H[0])*180/math.pi
            myTurtle.setheading(initial+head)
            myTurtle.pendown()

    scrTurtle.exitonclick()

if __name__ == "__main__":
    # initial = raw_input("initial?")
    # n_rules = input("how many rules?")
    initial = 'A(100,30)'
    n_rules = 1
    rules = []
    for i in range(n_rules):
        # s = raw_input("# %s rule: " %str(i+1))
        # s = "A(s,w):s>=0.5 -> !(w)F(s)[()+(25)/(180)A(s*0.5,w*0.45**0.5)]()[()+(-15)/(0)A(s*0.77,w*0.55**0.5)]()"
        s = "A(s,w):s>=0 -> !(w)F(s)[()+(35)/(0)A(s*0.75,w*0.5**0.4)]()[()+(-35)/(0)A(s*0.77,w*0.5**0.4)]()"

        rules.append(s)
        
    # n = input("how many iterations?")
    n = 5

    functions = {}
    for i in range(n_rules):
        func_name, paras, cond, expr = parse(rules[i])
        functions[func_name] = (paras, cond, expr)
    
    action_list = intrp_expr(initial)
    print action_list
    all_actions = unfold(action_list, functions, n)
    print "after unfold: ", all_actions
    execute(all_actions)

