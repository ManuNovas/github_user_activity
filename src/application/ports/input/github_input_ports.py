from abc import ABC, abstractmethod


class GithubInputPort(ABC):
    @abstractmethod
    def get_activity(self, user: str, activity_type: str | None) -> list[str]:
        pass
