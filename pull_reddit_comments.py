import typing, requests, json
import praw, os, urllib.parse
from praw.models import MoreComments
from collections import deque


BASE_URL = 'https://www.reddit.com/r/russian/'

reddit = praw.Reddit('NLPTesting')

subreddit = reddit.subreddit('russian')

all_comments = []



for submission in subreddit.top(limit = 10):
    submission.comments.replace_more(limit=None)
    queue, results = deque(submission.comments.list()), []
    while queue:
        comment = queue.popleft()
        results.append({'permalink': comment.permalink, 'body': comment.body})
        queue.extend(comment.replies)

    with open('r_russian_reddit_comments.jsonl', 'a') as f:
        f.write('\n'.join(map(json.dumps, results)))

