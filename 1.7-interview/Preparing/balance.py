from stack import Stack


def balance(string: str):
    open_brackets = ['(', '[', '{']
    closing_brackets = [')', ']', '}']
    matches = [('(', ')'), ('[', ']'), ('{', '}')]
    if len(string) % 2 == 1 or string[0] not in open_brackets or string[-1] not in closing_brackets:
        return 'Несбалансированно'
    stack = Stack()
    for item in string:
        if item in open_brackets:
            stack.push(item)
        else:
            top_stack = stack.pop()
            if (top_stack, item) not in matches:
                return 'Несбалансированно'

    if stack.isEmpty():
        return 'Сбалансированно'
