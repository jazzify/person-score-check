from abc import ABC, abstractmethod

from src.utils.server_simulator import NationalArchivesServer, NationalRegistryServer


class ExternalSystemService(ABC):
    def __init__(self, user: dict) -> None:
        self.user = user
        self.is_valid: bool = False

    @abstractmethod
    async def user_validator_score(self) -> dict:
        pass

    def _set_is_valid(self, is_valid: bool) -> None:
        self.is_valid = is_valid

    def _get_is_valid(self) -> bool:
        return self.is_valid


class NationalRegistrySystemService(ExternalSystemService):
    async def user_validator_score(self) -> float:
        registry_server = NationalRegistryServer(self.user)
        external_validator = await registry_server.get_user_score()
        self._set_is_valid(external_validator["is_valid"])
        return self._get_is_valid()


class NationalArchivesSystemService(ExternalSystemService):
    async def user_validator_score(self) -> float:
        archive_server = NationalArchivesServer(self.user)
        external_validator = await archive_server.get_user_score()
        self._set_is_valid(external_validator["is_valid"])
        return self._get_is_valid()
