#!/usr/bin/python3
"""Module for querying the Reddit API for subreddit information."""
import requests

def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Mozilla/5.0'}

    # Make API request and prevent redirects
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Return number of subscribers if response is successful
    if response.status_code == 200:
        data = response.json()
        return data.get('data', {}).get('subscribers', 0)
    return 0

