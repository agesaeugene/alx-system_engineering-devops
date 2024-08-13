#!/usr/bin/python3
"""Function for printing hot posts on a specific Reddit subreddit."""
import requests


def top_ten(subreddit):
    """
    Titles of the 10 hottest posts on a given
    subreddit are printed
    """
    response = requests.get(
        f"https://www.reddit.com/r/{subreddit}/hot.json",
        headers={"User-Agent": "Mozilla/5.0"},
        allow_redirects=False,
        params={"limit": 10}
    )

    # Checks response if it was successful or not redirect
    if response.status_code != 200 or response.is_redirect:
        print(None)
        return

    # Parse the JSON response to get the number of subscribers
    try:
        data = response.json()
        for post in data["data"]["children"]:
            print(post["data"]["title"])
    except (KeyError, ValueError):
        print(None)
        return
