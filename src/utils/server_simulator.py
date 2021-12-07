from asyncio import sleep as asleep
from random import uniform

from src.config.databases import ARCHIVES_VALID_USERS, REGISTRY_VALID_USERS


class ExternalServer:
    def __init__(self, user: dict) -> None:
        self.user = user
        self.response = {}

    async def get_user_score(self) -> None:
        # Simulate server latency between 300 and 1000 ms
        t = uniform(0.3, 1)
        await asleep(t)
        return self._get_response()

    def _get_response(self):
        return self.response


class NationalRegistryServer(ExternalServer):
    async def get_user_score(self) -> None:
        is_valid = self.user["id"] in REGISTRY_VALID_USERS
        self.response = {"user": self.user["name"], "is_valid": is_valid}
        return await super().get_user_score()


class NationalArchivesServer(ExternalServer):
    async def get_user_score(self) -> None:
        is_valid = self.user["name"] in ARCHIVES_VALID_USERS
        self.response = {"user": self.user["name"], "is_valid": is_valid}
        return await super().get_user_score()
