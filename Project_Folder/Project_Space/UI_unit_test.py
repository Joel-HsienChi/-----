import unittest
import UI_MySQL

class TestUI(unittest.TestCase):

        def test_open_concentrate_window(self):
                UI_MySQL.UI_Login_function().show_normal_welcome_message()





if __name__ == '__main__':
        unittest.main()