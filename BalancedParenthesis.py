def CheckIfBalanced(Expression):
    stack = []
    for i in range(len(Expression)):
        if Expression[i] == "[" or Expression[i] == "(" or Expression[i] == "{":
            stack.append(Expression[i])
        elif Expression[i] == "]":
            last = stack.pop()
            if last != "[":
                stack.append(last)
                break
        elif Expression[i] == "}":
            last = stack.pop()
            if last != "{":
                stack.append(last)
                break
        elif Expression[i] == ")":
            last = stack.pop()
            if last != "(":
                stack.append(last)
                break
    if not stack:
        print("The expression is balanced")
        return True
    else:
        print("Unbalanced expression")
        return False
        

Expression = '[{())]'
Balanced = CheckIfBalanced(Expression)
