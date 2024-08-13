#!/usr/bin/python3
import requests


def count_words(subreddit, word_list):
    """
    Parses the title of all hot articles and publishes a sorted
    count of the provided keywords (case-insensitive, separated
    by spaces). Javascript should count as javascript, but java 
    should not.
    """
    # initializes the counts dict on first call
    counts = {}

    # setting up the Reddit API endpoint URL
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    # setting the user agent header to avoid 429 errors
    headers = {"User-Agent": "Mozilla/5.0"}

    # sends a GET request to the Reddit API
    response = requests.get(url, headers=headers)

    # if the subreddit is invalid or there is an
    if response.status_code != 200:
        return

    # extracts JSON data from the response
    data = response.json()

    # loops through the list of posts and extract the titles
    for post in data["data"]["children"]:
        title = post["data"]["title"]

        # loops through the list of words and count their
        for word in word_list:
            # ensure the word is in lowercase and remove any
            word = word.lower().strip(".,!?:;")

            # count the number of occurrences of the word
            count = title.lower().count(word)

            # adds the count to the counts dict
            if count > 0:
                if word in counts:
                    counts[word] += count
                else:
                    counts[word] = count

    # if there are no results, return 0
    if not counts:
        return

    # sort results by count (descending) and then by word (ascending)
    sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))

    # print the results
    for word, count in sorted_counts:
        print(f"{word}: {count}")
