#!/usr/bin/python3
"""Function for querrying subscribers on a given subreddit"""
import requests

def number_of_subscribers(subreddit):
    """gives back the total number of members on a specific subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
            "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/eugene)"
    }
    response = requesr.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    results = response.json().get("data")
    return result.get("subscribers")

