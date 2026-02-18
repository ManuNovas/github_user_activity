from requests import get
from src.application.ports.output import GithubOutputPort


class GithubOutputAdapter(GithubOutputPort):
    URL = "https://api.github.com"

    def get_user_activity(self, user: str) -> list:
        url = f"{self.URL}/users/{user}/events"
        headers = {
            "Accept": "application/vnd.github+json"
        }
        response = get(url=url, headers=headers)
        if response.status_code == 200:
            user_activity = response.json()
        else:
            print(f"Service failed with status code {response.status_code}")
            user_activity = []
        return user_activity
