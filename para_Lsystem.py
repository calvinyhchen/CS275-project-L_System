# w = A(100, 30)
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

def parse(axiom, string, n):
    func, string = string.split(':')
    print func, string
    func_name, paras, _ = get_content(func)
    print func_name, paras.split(',')

    cond, expr = string.split('->')
    print cond, expr
    
    cond = intrp_cond(cond)
    expr = intrp_expr(expr)
    print cond, expr

    return 
    # for _ in range(n):


if __name__ == "__main__":
    axiom = raw_input("initial?")
    string = raw_input("rules?")
    n = raw_input("iterations?")
    parse(axiom, string, n)