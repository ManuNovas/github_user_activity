from src.application.ports.builders import GithubBuilderPort
from src.application.ports.input import GithubInputPort
from src.application.ports.output import GithubOutputPort


class GithubUseCases(GithubInputPort):
    output: GithubOutputPort
    builder: GithubBuilderPort

    def __init__(self, output: GithubOutputPort, builder: GithubBuilderPort):
        self.output = output
        self.builder = builder

    def get_activity(self, user: str):
        activities = self.output.get_user_activity(user)
        return self.builder.build_activities(activities)
