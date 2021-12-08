from abc import ABC, abstractmethod
from random import randint


class InternalSystemService(ABC):
    def __init__(self, scores: list[str]) -> None:
        self.scores = scores
        self.user_score: int = 0
        self.set_user_score()

    @abstractmethod
    def verify_validations(self) -> bool:
        pass

    @abstractmethod
    def set_user_score(self) -> int:
        pass

    @abstractmethod
    def is_prospect_user(self) -> bool:
        pass

    def get_user_score(self) -> int:
        return self.user_score


class ProspectQualificationSystemService(InternalSystemService):
    def verify_validations(self) -> bool:
        return all(self.scores)

    def set_user_score(self) -> None:
        if self.verify_validations():
            self.user_score = randint(0, 100)

    def is_prospect_user(self) -> bool:
        return self.get_user_score() > 60
