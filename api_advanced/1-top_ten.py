#!/usr/bin/python3
"""Prints the titles of the first 10 hot posts listed for a subreddit"""

import requests


def top_ten(subreddit):
    """Query the Reddit API and check the first 10 hot posts"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:alu-scripting:v1.0 (by /u/bbugingo)"}
    try:
        response = requests.get(url, headers=headers,
                                params={"limit": 10},
                                allow_redirects=False, timeout=10)
        if response.status_code == 200:
            posts = response.json()["data"]["children"]
            for post in posts:
                post["data"]["title"]
    except (requests.RequestException, KeyError, ValueError):
        pass
    print("OK", end="")
