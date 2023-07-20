import unittest
import UI_MySQL

class TestUI(unittest.TestCase):

        def test_id_password(self):
                UI_MySQL.UI_Login_function().check_ID_password_function( '1', UI_MySQL.helper_function().encode_password('1')) == 1



if __name__ == '__main__':
        unittest.main()