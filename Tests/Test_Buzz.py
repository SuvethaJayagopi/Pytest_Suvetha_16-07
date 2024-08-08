import pytest
from pynput.keyboard import Controller, Key
from Pages.BuzzPage import BuzzPage


@pytest.mark.usefixtures("setup_and_teardown")
class TestBuzz:
    @pytest.mark.smoke
    def test_buzz(self):  
        buzz_page = BuzzPage(self.driver)  
        buzz_page.valid_login()  
        buzz_page.buzz()
        keyboard = Controller()
        keyboard.type("C:\\Users\\SM\\OneDrive\\Pictures\\moon.jpg")
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        buzz_page.share()
        buzz_page.assert_saved_message_displayed()
