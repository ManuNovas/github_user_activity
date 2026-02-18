from abc import ABC, abstractmethod


class GithubInputPort(ABC):
    @abstractmethod
    def get_activity(self, user: str) -> list[str]:
        pass
