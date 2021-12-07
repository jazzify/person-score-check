import unittest

from src.controller import ValidatorController


class TestStringMethods(unittest.TestCase):
    def setUp(self):
        self.users = [
            {"id": "1151959064", "name": "Jorge"},
            {"id": "21429829", "name": "Miguel"},
            {"id": "1438277384", "name": "Karen"},
            {"id": "14382774", "name": "Julia"},
            {"ids": "14382774", "names": "Julia"},
        ]
        self.validator_controller = ValidatorController(self.users)

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
