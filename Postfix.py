import operator
import InfixToPostfix
from decimal import Decimal
ops = {'+': operator.add, '-': operator.sub, '*':operator.mul, '/':operator.truediv, '^':operator.pow}

infix_exp = '4*((1+5)/2)'
postfix_exp = InfixToPostfix.Infix2Postfix(infix_exp)
print(f"The postfix expression is {postfix_exp}")

stack = []
try:
    for i in range(len(postfix_exp)):
        if postfix_exp[i].isnumeric():
            stack.append(postfix_exp[i])
        else:
            a = stack.pop()
            b = stack.pop()
            if postfix_exp[i] == '-' or postfix_exp[i] == '/' or postfix_exp[i] == '^':
                c = ops[postfix_exp[i]](Decimal(b),Decimal(a))
            else:
                c = ops[postfix_exp[i]](Decimal(a),Decimal(b))
            stack.append(str(c)) 
    if len(stack) > 1:
        print('Wrong balance of numbers and operands')
    else:          
        print(f'The result is {stack.pop()}')
except Exception as e: print(e)
    #print('Wrong balance of numbers and operands')