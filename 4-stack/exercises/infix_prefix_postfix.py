# Push element at the bottom of the stack

# Time Complexity:  O(n)

def precedence(x):
    if x == '(':
        return 0
    if x == '+' or x == '-':
        return 1
    if x == '*' or x == '/' or x == '%':
        return 2
    if x == '^':
        return 3
    return 4

def infix2postfix(expn):
    stk = []
    token_list = expn.split()
    output = ""
    for token in token_list:
        if token in '+-*/^%':
            while len(stk) != 0 and precedence(token) <= precedence(stk[len(stk) - 1]):
                outsrt = stk.pop()
                output = output + " " + outsrt
            stk.append(token)
        elif token == '(':
            stk.append(token)
        elif token == ')':
            outsrt = None
            while len(stk) != 0 and outsrt != '(':
                outsrt = stk.pop()
                if outsrt != '(':
                    output = output + " " + outsrt
        else:
            output = output + " " + token
    while len(stk) != 0:
        outsrt = stk.pop()
        output = output + " " + outsrt
    return output

def postfix_eval(expn):
    stk = []
    token_list = expn.split()
    for token in token_list:
        if token == '+':
            num1 = stk.pop()
            num2 = stk.pop()
            stk.append(num1 + num2)
        elif token == '-':
            num1 = stk.pop()
            num2 = stk.pop()
            stk.append(num1 - num2)
        elif token == '*':
            num1 = stk.pop()
            num2 = stk.pop()
            stk.append(num1 * num2)
        elif token == '/':
            num1 = stk.pop()
            num2 = stk.pop()
            stk.append(num1 / num2)
        else:
            stk.append(int(token))
    return stk.pop()

def main():
    expn = "10 + ((3))*5/(16-4)"
    postfix_expn = infix2postfix(expn)
    print("Infix: ", expn)
    print("Postfix: ", postfix_expn)
    eval_expn = "1 2 + 3 4 + *"
    print(eval_expn)
    print(postfix_eval(eval_expn))

if __name__ == "__main__":
    main()