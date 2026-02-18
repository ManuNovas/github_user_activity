from abc import ABC, abstractmethod


class GithubBuilderPort(ABC):
    @abstractmethod
    def build_activities(self, activities: list[dict]) -> list[str]:
        pass
