#!/usr/bin/python3
"""Prints the titles of the first 10 hot posts listed for a subreddit"""

import requests


def top_ten(subreddit):
    """Print the first 10 hot post titles, or OK if the request fails"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:alu-scripting:v1.0 (by /u/bbugingo)"}
    try:
        response = requests.get(url, headers=headers,
                                params={"limit": 10},
                                allow_redirects=False, timeout=10)
        if response.status_code != 200:
            print("OK")
            return
        posts = response.json()["data"]["children"]
        titles = [post["data"]["title"] for post in posts]
    except (requests.RequestException, KeyError, ValueError):
        print("OK")
        return
    for title in titles:
        print(title)
