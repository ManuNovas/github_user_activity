from src.application.ports.builders import GithubBuilderPort
from src.domain.enums import ActivityType


class GithubBuilderAdapter(GithubBuilderPort):
    def build_activities(self, activities: list[dict], activity_type: str | None) -> list[str]:
        messages = []
        try:
            filter = ActivityType(activity_type) if activity_type is not None else None
            for activity in activities:
                type = ActivityType(activity["type"])
                if activity_type is not None and filter != type:
                    continue
                repo_name = activity["repo"]["name"]
                if type == ActivityType.COMMIT_COMMENT:
                    message = f"Created a commit comment in {repo_name}"
                elif type == ActivityType.CREATE:
                    ref = activity["payload"]["ref_type"]
                    message = f"Created a new {ref} in {repo_name}"
                elif type == ActivityType.DELETE:
                    ref = activity["payload"]["ref_type"]
                    message = f"Deleted a {ref} in {repo_name}"
                elif type == ActivityType.DISCUSSION:
                    message = f"Created a discussion in {repo_name}"
                elif type == ActivityType.FORK:
                    message = f"Forked a repository from {repo_name}"
                elif type == ActivityType.GOLLUM:
                    message = f"Created or updated a wiki page in {repo_name}"
                elif type == ActivityType.ISSUE_COMMENT:
                    message = f"Commented on an issue in {repo_name}"
                elif type == ActivityType.ISSUES:
                    message = f"Open a new issue in {repo_name}"
                elif type == ActivityType.MEMBER:
                    action = activity["payload"]["action"]
                    message = f"A member was {action} in {repo_name}"
                elif type == ActivityType.PUBLIC:
                    message = f"Changed {repo_name} to public"
                elif type == ActivityType.PULL_REQUEST:
                    action = activity["payload"]["action"]
                    message = f"A pull request was {action} in {repo_name}"
                elif type == ActivityType.PULL_REQUEST_REVIEW:
                    action = activity["payload"]["action"]
                    message = f"A pull request review was {action} in {repo_name}"
                elif type == ActivityType.PULL_REQUEST_REVIEW_COMMENT:
                    action = activity["payload"]["action"]
                    message = f"A pull request review comment was {action} in {repo_name}"
                elif type == ActivityType.PUSH:
                    message = f"Pushed a commit in {repo_name}"
                elif type == ActivityType.RELEASE:
                    action = activity["payload"]["action"]
                    message = f"A release was {action} in {repo_name}"
                elif type == ActivityType.WATCH:
                    message = f"Starred {repo_name}"
                if message is not None:
                    messages.append(message)
        except Exception as e:
            print(e)
        return messages
