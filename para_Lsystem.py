# w = A(100, w0)
# A(s, w):s>=min ->!(w)F(s)[+(35)/(0)A(s*0.75, w*q^e)][+(-35)/0A(s*0.77, w*(1-q)^e)]
def get_content(string):
    p = string.find('(')
    q = string.find(')')

    return string[:p], string[p+1:q], string[min(q+1, len(string)-1):]

def parse(axiom, string, n):
    func, string = string.split(':')
    print func, string
    name, paras, _ = get_content(func)
    print name, paras.split(',')

    condition, expr = string.split('->')
    print condition, expr

    # for _ in range(n):


if __name__ == "__main__":
    axiom = raw_input("initial?")
    string = raw_input("rules?")
    n = raw_input("iterations?")
    parse(axiom, string, n)