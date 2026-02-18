from unittest import TestCase
from unittest.mock import patch, MagicMock

from src.adapters.output import GithubOutputAdapter


class GithubOutputAdapterTest(TestCase):
    adapter: GithubOutputAdapter

    def setUp(self):
        self.adapter = GithubOutputAdapter()

    @patch("src.adapters.output.github_output_adapters.get")
    def test_get_user_activity(self, get_mock):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = [
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
        get_mock.return_value = mock_response
        user = "octocat"
        user_activity = self.adapter.get_user_activity(user)
        self.assertEqual(user_activity[0]["actor"]["login"], user)

    @patch("src.adapters.output.github_output_adapters.get")
    def test_get_user_activity_not_found(self, get_mock):
        mock_response = MagicMock()
        mock_response.status_code = 404
        get_mock.return_value = mock_response
        user = "octocat404"
        user_activity = self.adapter.get_user_activity(user)
        self.assertEqual(user_activity, [])
        self.assertLogs("404")
