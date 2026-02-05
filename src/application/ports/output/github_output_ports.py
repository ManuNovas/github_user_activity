from abc import ABC, abstractmethod


class GithubOutputPort(ABC):
    @abstractmethod
    def get_user_activity(self, user: str) -> list | None:
        pass
