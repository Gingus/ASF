# Created by gingu at 21/07/2021
Feature: login screen
  Testing the login screen, user field, password field, unsuccessful logins, successful login, using pytest-bdd

  Scenario: login_incorrect_user_password
    Given user is at the login screen
    When user enters 'incorrect' username and incorrect password
    Then an error is displayed on screen




#    Scenario: login_incorrect_password
#    Given user is at the login screen
#    When the user enters correct username and incorrect password in the fields
#    Then an error is display on screen
#
#
#  Scenario: login_incorrect_username
#    Given user is at the login screen
#    When the user enters incorrect username in the field # And correct password
#    Then an error is displayed on screen
#
#
#  Scenario: login_correct_user_password
#    Given user is at the login screen
#    When the user enters incorrect password in the field # And correct username
#    Then an error is display on screen