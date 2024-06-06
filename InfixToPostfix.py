import operator
ops = {'+': operator.add, '-': operator.sub, '*':operator.mul, '/':operator.truediv, '^':operator.pow}

def precedence(c):
    if c == '^':
        return 3
    elif c == '/' or c == '*':
        return 2
    elif c == '+' or c == '-':
        return 1
    else:
        return -1
    
def associativity(c):
    if c == '^':
        return False # Right
    return True  # Left


def Infix2Postfix(Expression):
    stack = []
    postfix = ''
    for i in range(len(Expression)):
        if Expression[i].isnumeric() or Expression[i].isalpha():
            postfix = postfix + Expression[i]
        elif Expression[i] == ")":
            while stack and stack[-1] != '(':
                postfix = postfix + stack.pop()
            stack.pop()
        elif Expression[i] == "(":
            stack.append(Expression[i])
        else:
            if stack:
                if precedence(Expression[i]) > precedence(stack[-1]):
                    stack.append(Expression[i])                
                elif stack[-1] == '(':
                    stack.append(Expression[i])
                else:
                    while stack and precedence(Expression[i]) <= precedence(stack[-1]) and associativity(Expression[i]):
                        postfix = postfix + stack.pop()
                    stack.append(Expression[i])
            else:
                stack.append(Expression[i])
            
    while stack:
        postfix = postfix + stack.pop()
    return postfix 



Expression = '4*((2+3)-6)/3'
print(Infix2Postfix(Expression))