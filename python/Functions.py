def do_math(num1, num2):
    result = num1 + num2
    result = result + 10
    result = result / 1.5
    result = result - num1
    return result

print(do_math(5,7))
print(do_math(8,19))
print(do_math(3,15))

import operator
print(operator.add(2,2))
print(operator.not_(True)) #not True
