from models.user import UserModel
from tests.unit.unit_base_test import UnitBaseTest


class UserTest(UnitBaseTest):
    def test_crete_user(self):
        user = UserModel('test', 'asdf')

        self.assertEqual(user.username, 'test',
                         "Something lo beseder.")
        self.assertEqual(user.password, 'asdf',
                         "Something lo beseder.")












































