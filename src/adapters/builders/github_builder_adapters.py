from src.application.ports.builders import GithubBuilderPort


class GithubBuilderAdapter(GithubBuilderPort):
    def build_activities(self, activities: list[dict]) -> list[str]:
        messages = []
        for activity in activities:
            type = activity["type"]
            repo_name = activity["repo"]["name"]
            if type == "CommitCommentEvent":
                message = f"Created a commit comment in {repo_name}"
            elif type == "CreateEvent":
                ref = activity["payload"]["ref_type"]
                message = f"Created a new {ref} in {repo_name}"
            elif type == "DeleteEvent":
                ref = activity["payload"]["ref_type"]
                message = f"Deleted a {ref} in {repo_name}"
            elif type == "DiscussionEvent":
                message = f"Created a discussion in {repo_name}"
            elif type == "ForkEvent":
                message = f"Forked a repository from {repo_name}"
            elif type == "GollumEven":
                message = f"Created or updated a wiki page in {repo_name}"
            elif type == "IssueCommentEvent":
                message = f"Commented on an issue in {repo_name}"
            elif type == "IssuesEvent":
                message = f"Open a new issue in {repo_name}"
            elif type == "MemberEvent":
                action = activity["payload"]["action"]
                message = f"A member was {action} in {repo_name}"
            elif type == "PublicEvent":
                message = f"Changed {repo_name} to public"
            elif type == "PullRequestEvent":
                action = activity["payload"]["action"]
                message = f"A pull request was {action} in {repo_name}"
            elif type == "PullRequestReviewEvent":
                action = activity["payload"]["action"]
                message = f"A pull request review was {action} in {repo_name}"
            elif type == "PullRequestReviewCommentEvent":
                action = activity["payload"]["action"]
                message = f"A pull request review comment was {action} in {repo_name}"
            elif type == "PushEvent":
                message = f"Pushed a commit in {repo_name}"
            elif type == "ReleaseEvent":
                action = activity["payload"]["action"]
                message = f"A release was {action} in {repo_name}"
            elif type == "WatchEvent":
                message = f"Starred {repo_name}"
            else:
                message = None
            if message is not None:
                messages.append(message)
        return messages
