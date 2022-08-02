from pytest_bdd import scenario, parsers, given, when, then
from loggingIn import *

@scenario('C:\\Users\\gingu\\PycharmProjects\\asf\\CodeTest\\tests\\features\\login.feature',
          'login_incorrect_user_password')
@given("user is at the login screen")
def test_login_reached():
    raise NotImplementedError(u'STEP: Given the user is at the login screen')


@when{parsers.cfparse("user enters "{incorrect:str}" username and incorrect password")}
def user_password_incorrect(incorrect):
    test_login_reached()
    select_user_field(incorrect)
    raise NotImplementedError(u'STEP: When the user enters "incorrect" username in the field # And incorrect password')


@then("an error is displayed on screen")
def step_impl():
    raise NotImplementedError(u'STEP: Then an error is displayed on screen')


# @scenario('C:\\Users\\gingu\\PycharmProjects\\asf\\CodeTest\\tests\\features\\login.feature',
#           'login_incorrect_username')
# @given("the user is at the login screen")
# def test_login_reached():
#     raise NotImplementedError(u'STEP: Given the user is at the login screen')
#
#
# @when("the user enters incorrect username in the field # And correct password")
# def user_incorrect():
#     raise NotImplementedError(u'STEP: When the user enters incorrect username in the field # And correct password')
#
#
# @then("an error is displayed on screen")
# def step_impl():
#     raise NotImplementedError(u'STEP: Then an error is displayed on screen')
#
#
# @scenario('C:\\Users\\gingu\\PycharmProjects\\asf\\CodeTest\\tests\\features\\login.feature',
#           'login_incorrect_user_password')
# @given("user is at the login screen")
# def test_login_reached():
#     raise NotImplementedError(u'STEP: Given the user is at the login screen')
#
#
# @when("the user enters incorrect password in the field # And correct username")
# def password_incorrect():
#     raise NotImplementedError(u'STEP: When the user enters incorrect password in the field # And correct username')
#
#
# @then("an error is display on screen")
# def step_impl():
#     raise NotImplementedError(u'STEP: Then an error is display on screen')
#
#
# @scenario('C:\\Users\\gingu\\PycharmProjects\\asf\\CodeTest\\tests\\features\\login.feature',
#           'login_correct_user_password')
# @given("user is at the login screen")
# def test_login_reached():
#     raise NotImplementedError(u'STEP: Given the user is at the login screen')
#
#
# @when("the user enters incorrect password in the field # And correct username")
# def user_password_correct():
#     raise NotImplementedError(u'STEP: When the user enters incorrect password in the field # And correct username')
#
#
# @then("user taken to logged in screen")
# def step_impl():
#     raise NotImplementedError(u'STEP: Then an error is display on screen')