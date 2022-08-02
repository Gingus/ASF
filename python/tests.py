import pytest

def fuzzy_math(num1, operator, num2):


    if type(num1) != int or type(num2) != int:
        raise Exception('We need to do fuzzy math on ints')
    else:
        pass

show_me = fuzzy_math()