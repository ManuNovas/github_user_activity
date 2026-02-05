from unittest import TestCase

from src.adapters.output import GithubOutputAdapter


class GithubOutputAdapterTest(TestCase):
    adapter: GithubOutputAdapter

    def setUp(self):
        self.adapter = GithubOutputAdapter()

    def test_get_user_activity(self):
        user = "ManuNovas"
        user_activity = self.adapter.get_user_activity(user)
        self.assertEqual(user_activity[0]["actor"]["login"], user)

    def test_get_user_activity_not_found(self):
        user = "ManuNovas404"
        user_activity = self.adapter.get_user_activity(user)
        self.assertEqual(user_activity, None)
        self.assertLogs("404")
