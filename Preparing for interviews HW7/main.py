from class_stack import Stack


def check_staples(date: list) -> bool:
    stack = Stack(date)
    working_stack = []
    while stack.is_empty():
        if stack.peek() in ['}', ']', ')']:
            pop = stack.pop()
            working_stack.append(pop)
        elif stack.peek() in ['(', '[', '{']:
            if len(working_stack) == 0:
                return False

            current_element = working_stack.pop()
            last_element = stack.pop()
            if current_element == ')' and last_element == '(':
                continue
            elif current_element == ']' and last_element == '[':
                continue
            elif current_element == '}' and last_element == '{':
                continue
    else:
        return True


if __name__ == '__main__':
    stack = list(input())
    print(check_staples(stack))
