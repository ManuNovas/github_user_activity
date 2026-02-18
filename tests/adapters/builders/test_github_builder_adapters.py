from unittest import TestCase

from src.adapters.builders import GithubBuilderAdapter


class TestGithubBuilderAdapter(TestCase):
    builder: GithubBuilderAdapter

    def setUp(self):
        self.builder = GithubBuilderAdapter()

    def test_build_activities(self):
        activities = [
            {
                "id": "22249084947",
                "type": "WatchEvent",
                "actor": {
                "id": 583231,
                "login": "octocat",
                "display_login": "octocat",
                "gravatar_id": "",
                "url": "https://api.github.com/users/octocat",
                "avatar_url": "https://avatars.githubusercontent.com/u/583231?v=4"
                },
                "repo": {
                "id": 1296269,
                "name": "octocat/Hello-World",
                "url": "https://api.github.com/repos/octocat/Hello-World"
                },
                "payload": {
                "action": "started"
                },
                "public": True,
                "created_at": "2022-06-09T12:47:28Z"
            },
            {
                "id": "22249084964",
                "type": "PushEvent",
                "actor": {
                "id": 583231,
                "login": "octocat",
                "display_login": "octocat",
                "gravatar_id": "",
                "url": "https://api.github.com/users/octocat",
                "avatar_url": "https://avatars.githubusercontent.com/u/583231?v=4"
                },
                "repo": {
                "id": 1296269,
                "name": "octocat/Hello-World",
                "url": "https://api.github.com/repos/octocat/Hello-World"
                },
                "payload": {
                "repository_id": 1296269,
                "push_id": 10115855396,
                "ref": "refs/heads/master",
                "head": "7a8f3ac80e2ad2f6842cb86f576d4bfe2c03e300",
                "before": "883efe034920928c47fe18598c01249d1a9fdabd"
                },
                "public": True,
                "created_at": "2022-06-07T07:50:26Z"
            }
        ]
        messages = self.builder.build_activities(activities)
        self.assertEqual(len(activities), len(messages))

    def test_build_invalid_activities(self):
        activities = activities = [
            {
                "id": "22249084947",
                "type": "WatchedEvent",
                "actor": {
                "id": 583231,
                "login": "octocat",
                "display_login": "octocat",
                "gravatar_id": "",
                "url": "https://api.github.com/users/octocat",
                "avatar_url": "https://avatars.githubusercontent.com/u/583231?v=4"
                },
                "repo": {
                "id": 1296269,
                "name": "octocat/Hello-World",
                "url": "https://api.github.com/repos/octocat/Hello-World"
                },
                "payload": {
                "action": "started"
                },
                "public": True,
                "created_at": "2022-06-09T12:47:28Z"
            },
            {
                "id": "22249084964",
                "type": "PushedEvent",
                "actor": {
                "id": 583231,
                "login": "octocat",
                "display_login": "octocat",
                "gravatar_id": "",
                "url": "https://api.github.com/users/octocat",
                "avatar_url": "https://avatars.githubusercontent.com/u/583231?v=4"
                },
                "repo": {
                "id": 1296269,
                "name": "octocat/Hello-World",
                "url": "https://api.github.com/repos/octocat/Hello-World"
                },
                "payload": {
                "repository_id": 1296269,
                "push_id": 10115855396,
                "ref": "refs/heads/master",
                "head": "7a8f3ac80e2ad2f6842cb86f576d4bfe2c03e300",
                "before": "883efe034920928c47fe18598c01249d1a9fdabd"
                },
                "public": True,
                "created_at": "2022-06-07T07:50:26Z"
            }
        ]
        messages = self.builder.build_activities(activities)
        self.assertEqual(len(messages), 0)
