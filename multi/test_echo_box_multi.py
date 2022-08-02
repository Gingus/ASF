def test_echo_box(home):
    """created the first test for echo box"""
    echo = home.nav_to_echo_box()

    message = 'Hello'
    echo.save_message(message)
    assert echo.read_message() == message
    home = echo.nav_back()

    echo = home.nav_to_echo_box()
    assert echo.read_message() == message


def test_saved_message_is_empty_to_start(home):
    """Testing if there is no text present"""
    echo = home.nav_to_echo_box()
    assert echo.read_message() is None

# Notes for command line
# pytest --platform=android test_echo_box()
# pytest --platform=ios test_echo_box()
# from the Terminal
