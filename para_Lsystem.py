# A(100, 30)
# A(s, w):s>=0 ->!(w)F(s)[+(35)/(0)A(s*0.75, w*(0.5)^(0.4)))][+(-35)/(0)A(s*0.77, w*(0.5)^(0.4))]
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

def execute(all_actions):
    for (func, para) in all_actions:
        if func == '!':

        elif func == '/':
        
        elif func == '+':
        
        elif func == '-':
        
        elif func == 'F':
        
        elif func == '[':
        
        elif func == ']':


if __name__ == "__main__":
    # initial = raw_input("initial?")
    # n_rules = input("how many rules?")
    initial = 'A(100,30)'
    n_rules = 1
    rules = []
    for i in range(n_rules):
        # s = raw_input("# %s rule: " %str(i+1))
        s = "A(s,w):s>=0 -> !(w)F(s)[()+(35)/(0)A(s*0.75,w*0.5**0.4)]()[()+(-35)/(0)A(s*0.77,w*0.5**0.4)]()"
        rules.append(s)
        
    # n = input("how many iterations?")
    n = 3

    functions = {}
    for i in range(n_rules):
        func_name, paras, cond, expr = parse(rules[i])
        functions[func_name] = (paras, cond, expr)
    
    action_list = intrp_expr(initial)
    print action_list
    all_actions = unfold(action_list, functions, n)
    print "after unfold: ", all_actions
    execute(all_actions)

