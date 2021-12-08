from abc import ABC, abstractmethod


class Validator(ABC):
    @abstractmethod
    def get_validated_data(self):
        pass

    @abstractmethod
    def validate(self):
        pass


class UserControllerValidator(Validator):
    def __init__(self, users: list[dict]) -> None:
        self.users = users
        self.valid_users: list[dict] = []
        self.invalid_users: list[dict] = []
        self.validate()

    def get_validated_data(self) -> list[dict]:
        return self.valid_users

    def validate(self) -> None:
        for user in self.users:
            # Checks 'id' and 'name' exists
            if user.keys() >= {"id", "name"}:
                # Checks 'id' and 'name' values are str instances
                if map(
                    lambda k: isinstance(k, str),
                    [user["id"], user["name"]],
                ):
                    self.valid_users.append(user)
            else:
                self.invalid_users.append(user)

        print(f"Invalid users: {self.invalid_users}")
