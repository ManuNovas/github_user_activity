from enum import Enum


class ActivityType(Enum):
    COMMIT_COMMENT = "CommitCommentEvent"
    CREATE = "CreateEvent"
    DELETE = "DeleteEvent"
    DISCUSSION = "DiscussionEvent"
    FORK = "ForkEvent"
    GOLLUM = "GollumEven"
    ISSUE_COMMENT = "IssueCommentEvent"
    ISSUES = "IssuesEvent"
    MEMBER = "MemberEvent"
    PUBLIC = "PublicEvent"
    PULL_REQUEST = "PullRequestEvent"
    PULL_REQUEST_REVIEW = "PullRequestReviewEvent"
    PULL_REQUEST_REVIEW_COMMENT = "PullRequestReviewCommentEvent"
    PUSH = "PushEvent"
    RELEASE = "ReleaseEvent"
    WATCH = "WatchEvent"
