def check(s):
    stack = []
    char_n = 0

    for char in s:
        char_n += 1

        if char not in ('(', '[', '{', '}', ']', ')'):
            continue

        if char in ('(', '[', '{'):
            stack.append(char)
        
        elif len(stack) == 0:
            return char_n

        else:

            if (char == ')' and stack[-1] == '(') or (char == ']' and stack[-1] == '[') or (char == '}' and stack[-1] == '{'):
                stack.pop()

            else:
                return char_n
            

    return 0 if len(stack) == 0 else len(stack)

if __name__ == '__main__':
    #print(check(input())) 'Success'

    print(check("{*{{}"))

    assert check("([](){([])})") == 0
    assert check("()[]}") == 5
    assert check("{{[()]]") == 7
    assert check("{{{[][][]") == 3
    assert check("{*{{}") == 3
    assert check("[[*") == 2
    assert check("{*}") == 0
    assert check("{{") == 2
    assert check("{}") == 0
    assert check("") == 0
    assert check("}") == 1
    assert check("*{}") == 0
    assert check("{{{**[][][]") == 3