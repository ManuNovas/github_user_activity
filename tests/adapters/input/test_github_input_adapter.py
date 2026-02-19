from unittest import TestCase
from unittest.mock import MagicMock

from src.adapters.builders import GithubBuilderAdapter
from src.adapters.input import GithubInputAdapter
from src.adapters.output import GithubOutputAdapter
from src.application.use_cases import GithubUseCases


class TestGithubInputAdapter(TestCase):
    input_adapter: GithubInputAdapter

    def setUp(self):
        output = GithubOutputAdapter()
        builder = GithubBuilderAdapter()
        use_cases = GithubUseCases(output, builder)
        use_cases.get_activity = MagicMock(return_value=[
            "CliveRosfield push a commit in CliveRosfield/FinalFantasyXVI",
        ])
        self.input_adapter = GithubInputAdapter(use_cases)

    def test_get_activity(self):
        result = self.input_adapter.main(["main.py", "CliveRosfield"])
        self.assertEqual(result, 0)
        self.assertLogs("CliveRosfield")

    def test_get_activity_without_user(self):
        result = self.input_adapter.main(["main.py"])
        self.assertEqual(result, 1)
