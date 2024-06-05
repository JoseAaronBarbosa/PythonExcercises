import operator
ops = {'+': operator.add, '-': operator.sub, '*':operator.mul, '/':operator.truediv, '^':operator.pow}

postfix_exp = '15+2/'
stack = []
try:
    for i in range(len(postfix_exp)):
        if postfix_exp[i].isnumeric():
            stack.append(postfix_exp[i])
        else:
            a = stack.pop()
            b = stack.pop()
            if postfix_exp[i] == '-' or postfix_exp[i] == '/' or postfix_exp[i] == '^':
                c = ops[postfix_exp[i]](int(b),int(a))
            else:
                c = ops[postfix_exp[i]](int(a),int(b))
            stack.append(str(c)) 
    if len(stack) > 1:
        print('Wrong balance of numbers and operands')
    else:          
        print(f'The result is {stack.pop()}')
except:
    print('Wrong balance of numbers and operands')