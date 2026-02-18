from unittest import TestCase
from unittest.mock import patch, MagicMock

from src.adapters.builders import GithubBuilderAdapter
from src.adapters.output import GithubOutputAdapter
from src.application.use_cases import GithubUseCases


class TestGithubUseCases(TestCase):
    use_cases: GithubUseCases

    def setUp(self):
        output = GithubOutputAdapter()
        builder = GithubBuilderAdapter()
        self.use_cases = GithubUseCases(output, builder)

    @patch("src.adapters.output.github_output_adapters.get")
    def test_get_activity(self, get_mock):
        activities = [
            {
                "type": "CommitCommentEvent",
                "repo": {
                    "name": "clive-rosfield/final-fantasy-xvi",
                },
            },
            {
                "type": "CreateEvent",
                "repo": {
                    "name": "clive-rosfield/final-fantasy-xvi",
                },
                "payload": {
                    "ref_type": "branch",
                },
            },
            {
                "type": "DeleteEvent",
                "repo": {
                    "name": "clive-rosfield/final-fantasy-xvi",
                },
                "payload": {
                    "ref_type": "branch",
                },
            },
        ]
        response_mock = MagicMock()
        response_mock.status_code = 200
        response_mock.json.return_value = activities
        get_mock.return_value = response_mock
        activity = self.use_cases.get_activity("clive-rosfield")
        self.assertEqual(len(activity), len(activities))
