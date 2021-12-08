from abc import ABC, abstractmethod

from src.utils.server_simulator import NationalArchivesServer, NationalRegistryServer


class ExternalSystemService(ABC):
    def __init__(self, user: dict) -> None:
        self.user = user
        self.is_valid: bool = False

    @abstractmethod
    async def validate_data(self, is_valid: bool) -> dict:
        self._set_is_valid(is_valid)
        return self._get_is_valid()

    def _set_is_valid(self, is_valid: bool) -> None:
        self.is_valid = is_valid

    def _get_is_valid(self) -> bool:
        return self.is_valid


class NationalRegistrySystemService(ExternalSystemService):
    async def validate_data(self, _: bool = False) -> dict:
        registry_server = NationalRegistryServer(self.user)
        external_validator = await registry_server.get_user_validation()
        return await super().validate_data(external_validator["is_valid"])


class NationalArchivesSystemService(ExternalSystemService):
    async def validate_data(self, _: bool = False) -> bool:
        archive_server = NationalArchivesServer(self.user)
        external_validator = await archive_server.get_user_validation()
        return await super().validate_data(external_validator["is_valid"])
