import unittest

from src.test.test_data import INVALID_USER, MIXED_USERS, VALID_USER, VALIDATED_USERS
from src.utils.server_simulator import NationalArchivesServer, NationalRegistryServer
from src.utils.validators import UserControllerValidator


class TestUtilsServer(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.valid_user = VALID_USER
        self.invalid_user = INVALID_USER

    async def test_national_registry_valid_user(self):
        registry_server = NationalRegistryServer(self.valid_user)
        external_validator = await registry_server.get_user_validation()

        self.assertEqual(
            external_validator, {"user": self.valid_user["name"], "is_valid": True}
        )

    async def test_national_registry_invalid_user(self):
        registry_server = NationalRegistryServer(self.invalid_user)
        external_validator = await registry_server.get_user_validation()

        self.assertEqual(
            external_validator, {"user": self.invalid_user["name"], "is_valid": False}
        )

    async def test_national_archives_valid_user(self):
        archives_server = NationalArchivesServer(self.valid_user)
        external_validator = await archives_server.get_user_validation()

        self.assertEqual(
            external_validator, {"user": self.valid_user["name"], "is_valid": True}
        )

    async def test_national_archives_invalid_user(self):
        archives_server = NationalArchivesServer(self.invalid_user)
        external_validator = await archives_server.get_user_validation()

        self.assertEqual(
            external_validator, {"user": self.invalid_user["name"], "is_valid": False}
        )


class TestUtilsValidators(unittest.TestCase):
    def setUp(self):
        self.mixed_users = MIXED_USERS
        self.validated_users = VALIDATED_USERS

    def test_user_controller_validator(self):
        user_controller_validator = UserControllerValidator(self.mixed_users)
        validated_users = user_controller_validator.get_validated_data()
        self.assertEqual(validated_users, self.validated_users)


if __name__ == "__main__":
    unittest.main()
