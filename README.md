# COSI230B-A0

## About

For the past five years, I have been teaching myself Russian, and one educational resource in particular that I have encountered on my quest is r/russian/, a forum of Russian language enthusiasts. For Part 1 of Homework 0, I used Praw to access the top 10 submissions on r/russian, and then subsequently pulled each submission's comments. There are several steps that my code performs:

* By default, Praw does [not return](https://praw.readthedocs.io/en/stable/tutorials/comments.html) every single comment on a submission, but instead, includes a `MoreComments` futures object which will fetch more comments on demand. To force all comments to be loaded into memory, I called `submission.comments.replace_more` with the parameter `limit = None` before storing the entire comment list by calling `submission.comments.list`. 
* `submission.comments.list` only returns the top level comments for the submission. However, I wanted to extract all comments, including replies. To do this, I used a breadth-first search to walk each `Comment` object and its replies by accessing the `Comment.replies` attribute

In the end, I mangaged to extract 4193 comments, formatted as a dataset called `r_russian_reddit_comments.jsonl`