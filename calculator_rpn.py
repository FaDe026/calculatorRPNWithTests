import operator
import re

OPS = {
    '+': (1, operator.add),
    '-': (1, operator.sub),
    '*': (2, operator.mul),
    '/': (2, operator.truediv),
    '**': (3, operator.pow),
}


def tokenize(expression):
    token_pattern = r'\d+\.?\d*|\*\*|[+\-*/()]'
    tokens = re.findall(token_pattern, expression)
    return tokens


def infix_to_rpn(tokens):
    out = []
    stack = []

    def precedence(op):
        return OPS[op][0]

    i = 0
    while i < len(tokens):
        token = tokens[i]

        if re.match(r'\d+\.?\d*', token):
            out.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                out.append(stack.pop())
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                raise ValueError("Mismatched parentheses")
        else:
            while (stack and stack[-1] in OPS and
                   ((precedence(stack[-1]) > precedence(token)) or
                    (precedence(stack[-1]) == precedence(token) and token != '**'))):
                out.append(stack.pop())
            stack.append(token)
        i += 1

    while stack:
        if stack[-1] in ('(', ')'):
            raise ValueError("Mismatched parentheses")
        out.append(stack.pop())
    return out


def eval_rpn(rpn_tokens):
    stack = []
    for token in rpn_tokens:
        if token in OPS:
            b = stack.pop()
            a = stack.pop()
            stack.append(OPS[token][1](a, b))
        else:
            stack.append(float(token))
    if len(stack) != 1:
        raise ValueError("Invalid RPN expression")
    return stack[0]


def calculate(expression):
    tokens = tokenize(expression)
    rpn = infix_to_rpn(tokens)
    return eval_rpn(rpn)


def main():
    print("Калькулятор с обратной польской нотацией.")
    print("Введите математическое выражение или empty для выхода.")
    while True:
        expr = input("Введите выражение: ").strip()
        if expr.lower() in ('', 'exit'):
            print("Выход из калькулятора.")
            break
        try:
            print("Записанное выражение: " + expr)
            tokens = tokenize(expr)
            rpn_expr = infix_to_rpn(tokens)
            print("Выражение в обратной польской нотации: " + ' '.join(rpn_expr))
            result = calculate(expr)
            print("Результат:", result)
        except Exception as e:
            print("Ошибка вычисления:", e)


if __name__ == "__main__":
    main()
