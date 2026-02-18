from unittest import TestCase

from src.adapters.builders import GithubBuilderAdapter


class TestGithubBuilderAdapter(TestCase):
    builder: GithubBuilderAdapter

    def setUp(self):
        self.builder = GithubBuilderAdapter()

    def test_build_activities(self):
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
            {
                "type": "DiscussionEvent",
                "repo": {
                    "name": "cloud-strife/final-fantasy-vii",
                },
            },
            {
                "type": "ForkEvent",
                "repo": {
                    "name": "cloud-strife/final-fantasy-vii",
                },
            },
            {
                "type": "GollumEven",
                "repo": {
                    "name": "clive-rosfield/final-fantasy-xvi",
                },
            },
            {
                "type": "IssueCommentEvent",
                "repo": {
                    "name": "cloud-strife/final-fantasy-vii",
                },
            },
            {
                "type": "IssuesEvent",
                "repo": {
                    "name": "cloud-strife/final-fantasy-vii",
                },
            },
            {
                "type": "MemberEvent",
                "repo": {
                    "name": "clive-rosfield/final-fantasy-xvi",
                },
                "payload": {
                    "action": "added",
                },
            },
            {
                "type": "PublicEvent",
                "repo": {
                    "name": "clive-rosfield/final-fantasy-xvi",
                },
            },
            {
                "type": "PullRequestEvent",
                "repo": {
                    "name": "cloud-strife/final-fantasy-vii",
                },
                "payload": {
                    "action": "added",
                },
            },
            {
                "type": "PullRequestReviewEvent",
                "repo": {
                    "name": "cloud-strife/final-fantasy-vii",
                },
                "payload": {
                    "action": "added",
                },
            },
            {
                "type": "PullRequestReviewCommentEvent",
                "repo": {
                    "name": "cloud-strife/final-fantasy-vii",
                },
                "payload": {
                    "action": "added",
                },
            },
            {
                "type": "PushEvent",
                "repo": {
                    "name": "clive-rosfield/final-fantasy-xvi",
                },
            },
            {
                "type": "ReleaseEvent",
                "repo": {
                    "name": "clive-rosfield/final-fantasy-xvi",
                },
                "payload": {
                    "action": "added",
                },
            },
            {
                "type": "WatchEvent",
                "repo": {
                    "name": "cloud-strife/final-fantasy-vii",
                },
            },
        ]
        messages = self.builder.build_activities(activities)
        self.assertEqual(len(activities), len(messages))

    def test_build_invalid_activities(self):
        activities = activities = [
            {
                "type": "CommitedCommentEvent",
                "repo": {
                    "name": "clive-rosfield/final-fantasy-xvi",
                },
            },
        ]
        messages = self.builder.build_activities(activities)
        self.assertEqual(len(messages), 0)
