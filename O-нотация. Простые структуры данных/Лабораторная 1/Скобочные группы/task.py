def check_brackets(brackets_row: str) -> bool:
    """
    Проверьте, является ли входная строка допустимой последовательностью скобок

    :param brackets_row: Входная строка для проверки
    :return: True, если последовательность корректна, False в противном случае
    """
    if not brackets_row:
        return True
    stack = []
    for i in brackets_row:
        if i=='(':
            stack.append(i)
        elif i==')':
            stack.clear()
    if not stack:
        return True
    else:
        return False



# TODO реализовать проверку скобочной группы


if __name__ == '__main__':
    print(check_brackets("()()"))  # True
    print(check_brackets(")("))  # False
