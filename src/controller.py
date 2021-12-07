import asyncio
from concurrent.futures import ProcessPoolExecutor

from src.services.external_systems_service import (
    NationalArchivesSystemService,
    NationalRegistrySystemService,
)
from src.services.internal_systems_service import ProspectQualificationSystemService


class ValidatorController:
    def __init__(self, users: dict) -> None:
        self.users = self._validated_users(users)
        self.user_validation = {}

    def _validated_users(self, users: list[dict]) -> list[dict]:
        valid_users = []
        invalid_users = []

        for user in users:
            # Checks 'id' and 'name' exists
            if user.keys() >= {"id", "name"}:
                # Checks 'id' and 'name' values are str instances
                if map(
                    lambda k: isinstance(k, str),
                    [user["id"], user["name"]],
                ):
                    valid_users.append(user)
            else:
                invalid_users.append(user)

        print(f"Invalid users: {invalid_users}")
        return valid_users

    def validate_users(self) -> dict:
        with ProcessPoolExecutor() as executor:
            for response in executor.map(self._run_validation, self.users):
                user = response["user"]
                scores = response["external_scores"]

                # Internal System
                prospect_service = ProspectQualificationSystemService(scores)
                internal_score = prospect_service.get_user_score()
                is_prospect = prospect_service.is_prospect_user()

                if not self.user_validation.get(user):
                    self.user_validation[user] = {}

                self.user_validation[user]["is_valid"] = scores
                self.user_validation[user]["internal_score"] = internal_score
                self.user_validation[user]["is_prospect"] = is_prospect

        return self.user_validation

    def _run_validation(self, user: dict) -> dict:
        return asyncio.run(self._get_user_validations(user))

    async def _get_user_validations(self, user: dict) -> dict:
        validations = {}
        validations["user"] = user["name"]

        # External Systems
        national_registry_system = NationalRegistrySystemService(user)
        national_archives_system = NationalArchivesSystemService(user)

        scores = await asyncio.gather(
            national_archives_system.user_validator_score(),
            national_registry_system.user_validator_score(),
        )

        validations["external_scores"] = scores
        return validations
