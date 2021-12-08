from asyncio import sleep as asleep
from random import uniform

from src.config.databases import ARCHIVES_VALID_USERS, REGISTRY_VALID_USERS


class ExternalServer:
    def __init__(self, user: dict) -> None:
        self.user = user
        self.response = {}

    async def get_user_validation(self, is_valid: bool) -> None:
        # Simulate server latency between 300 and 1000 ms
        t = uniform(0.3, 1)
        await asleep(t)
        self.response = {"user": self.user["name"], "is_valid": is_valid}
        return self._get_response()

    def _get_response(self):
        return self.response


class NationalRegistryServer(ExternalServer):
    async def get_user_validation(self, is_valid=False) -> dict:
        is_valid = self.user["id"] in REGISTRY_VALID_USERS
        return await super().get_user_validation(is_valid)


class NationalArchivesServer(ExternalServer):
    async def get_user_validation(self, is_valid=False) -> dict:
        is_valid = self.user["name"] in ARCHIVES_VALID_USERS
        return await super().get_user_validation(is_valid)
