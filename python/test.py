import pytest


def fuzzy_math(num1, operator, num2):

    if type(num1) != int or type(num2) != int:
        raise Exception('We need to do fuzzy math on ints')

    if operator == '+':
        result = num1 + num2
    elif operator == '*':
        result = num1 * num2
    else:
        raise Exception(f"I don't know how to do math with '{operator}'")

    if result < 0:
        return 'Negative number, what does that even mean'
    elif result < 10:
        return 'A small number, I can deal with that.'
    elif result < 20:
        return 'A medium sized number. OK.'
    else:
        return 'A really big number, way too big for me.'


class TestFuzzyMath:

    def test_non_int_input_for_num1(self):
        with pytest.raises(Exception) as exc_info:
            fuzzy_math('hi', '+', 2)
        assert 'fuzzy math on ints' in str(exc_info)

    # def test_non_int_input_for_num2(self):
    #     pass

    def test_addition_with_negative_result(self):
        with pytest.raises(Exception) as exec_info:
            fuzzy_math(2, '-', '4')
            assert 'Negative number' in str(exec_info)
            print(exec_info)

    def test_addition_with_small_result(self):
        with pytest.raises(Exception) as exec_info:
            fuzzy_math(2, '+', 2)
        assert 'A small number' in str(exec_info)

    def test_addition_with_medium_result(self):
        with pytest.raises(Exception) as exec_info:
            fuzzy_math(9, '+', 9)
        assert 'medium sized' in str(exec_info)

    def test_addition_with_large_result(self):
        with pytest.raises(Exception) as exec_info:
            fuzzy_math(2, '+', 22)
        assert 'really big' in str(exec_info)

    def test_multiplication_with_negative_result(self):
        with pytest.raises(Exception) as exec_info:
            fuzzy_math(2, '*', '-4')
            assert 'Negative number' in str(exec_info)

    def test_multiplication_with_small_result(self):
        with pytest.raises(Exception) as exec_info:
            fuzzy_math(2, '*', 2)
        assert 'A small number' in str(exec_info)

    def test_multiplication_with_medium_result(self):
        with pytest.raises(Exception) as exec_info:
            fuzzy_math(3, '*', 9)
        assert 'medium sized' in str(exec_info)

    def test_multiplication_with_large_result(self):
        with pytest.raises(Exception) as exec_info:
            fuzzy_math(3, '*', 6)
        assert 'really big' in str(exec_info)

    # def test_invalid_operator(self):
    #     pass
    #     with pytest.raises(Exception) as exec_info:
    #         while fuzzy_math.operator not in []
    #     assert 'really big' in str(exec_info)
