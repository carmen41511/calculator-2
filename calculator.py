"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code
while True:
    user_input = input('Enter your equation >')
    tokens = user_input.split()

    if tokens[0] == '+':
        ans = add(float(tokens[1]), float(tokens[2]))
        print(ans)

    elif tokens[0] == '-':
        ans = subtract(float(tokens[1]), float(tokens[2]))
        print(ans)

    elif tokens[0] == '*':
        ans = multiply(float(tokens[1]), float(tokens[2]))
        print(ans)
    
    elif tokens[0] == '/':
        ans = divide(float(tokens[1]), float(tokens[2]))
        print(ans)

    elif tokens[0] == 'square':
        ans = square(float(tokens[1]))
        print(ans)

    elif tokens[0] == 'cube':
        ans = cube(float(tokens[1]))
        print(ans)
    
    elif tokens[0] == 'pow':
        ans = power(float(tokens[1]), float(tokens[2]))
        print(ans)

    elif tokens[0] == 'mod':
        ans = mod(float(tokens[1]), float(tokens[2]))
        print(ans)

    else:
        break