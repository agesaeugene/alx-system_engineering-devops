#!/usr/bin/python3

import requests


def recurse(subreddit, hot_list=[], after=""):
    """
        Queries the Reddit API and returns a list of all article 
        titles for a specified subreddit. If there are no results 
        for the specified breddit, the method should return None.
    """
    # Make a request to the Reddit API to get the subreddit information
    response = requests.get(
        f"https://www.reddit.com/r/{subreddit}/hot.json",
        headers={"User-Agent": "Mozilla/5.0"},
        allow_redirects=False,
        params={"after": after}
    )

    # Checks wether respons was successful and not redirected
    if response.status_code != 200 or response.is_redirect:
        return None

    # Parse the JSON response to get the number of subscribers
    try:
        data = response.json()
        for post in data["data"]["children"]:
            hot_list.append(post["data"]["title"])
        after = data["data"]["after"]
        if after is None:
            return hot_list
        return recurse(subreddit, hot_list, after)
    except (KeyError, ValueError):
        return None
