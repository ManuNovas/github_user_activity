from src.application.ports.input import GithubInputPort


class GithubInputAdapter:
    input_port: GithubInputPort

    def __init__(self, input_port: GithubInputPort):
        self.input_port = input_port

    def main(self, argv: list[str]) -> int:
        if len(argv) < 2:
            print("You should specify a github user")
            return 1
        user = argv[1]
        activity_type = argv[2] if len(argv) > 2 else None
        activity = self.input_port.get_activity(user, activity_type)
        for a in activity:
            print(f"- {a}")
        return 0
