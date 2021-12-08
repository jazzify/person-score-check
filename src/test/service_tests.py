import unittest

from src.services.external_systems_service import (
    NationalArchivesSystemService,
    NationalRegistrySystemService,
)
from src.services.internal_systems_service import ProspectQualificationSystemService
from src.test.test_data import INVALID_USER, VALID_USER


class TestExternalServices(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.valid_user = VALID_USER
        self.invalid_user = INVALID_USER

    async def test_external_national_registry_valid_user(self):
        national_registry_system = NationalRegistrySystemService(self.valid_user)
        is_valid = await national_registry_system.validate_data()
        self.assertEqual(is_valid, True)

    async def test_external_national_registry_invalid_user(self):
        national_registry_system = NationalRegistrySystemService(self.invalid_user)
        is_valid = await national_registry_system.validate_data()
        self.assertEqual(is_valid, False)

    async def test_external_national_archives_valid_user(self):
        national_archives_system = NationalArchivesSystemService(self.valid_user)
        is_valid = await national_archives_system.validate_data()
        self.assertEqual(is_valid, True)

    async def test_external_national_archives_invalid_user(self):
        national_archives_system = NationalArchivesSystemService(self.invalid_user)
        is_valid = await national_archives_system.validate_data()
        self.assertEqual(is_valid, False)


class TestInternalServices(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.valid_user = VALID_USER
        self.invalid_user = INVALID_USER

    async def test_external_national_registry_valid_user(self):
        prospect_service = ProspectQualificationSystemService([True, True])
        internal_score = prospect_service.get_user_score()
        is_prospect = prospect_service.is_prospect_user()
        self.assertIn(internal_score, range(0, 101))
        self.assertEqual(is_prospect, internal_score > 60)

    async def test_external_national_registry_invalid_user(self):
        prospect_service = ProspectQualificationSystemService([True, False])
        internal_score = prospect_service.get_user_score()
        is_prospect = prospect_service.is_prospect_user()
        self.assertEqual(internal_score, 0)
        self.assertEqual(is_prospect, False)


if __name__ == "__main__":
    unittest.main()
