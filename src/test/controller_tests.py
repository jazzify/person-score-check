import unittest

from src.controller import ValidatorController
from src.test.test_data import MIXED_USERS


class TestController(unittest.TestCase):
    def setUp(self):
        self.validator_controller = ValidatorController(MIXED_USERS)

    def test_validate_users(self):
        validated_users = self.validator_controller.validate_users()

        self.assertEqual(len(validated_users), 4)
        for user in self.validator_controller.users:
            current_user = validated_users[user["name"]]
            self.assertEqual(len(current_user["is_valid"]), 2)
            self.assertIsInstance(current_user["internal_score"], int)
            self.assertIsInstance(current_user["is_prospect"], bool)


if __name__ == "__main__":
    unittest.main()
