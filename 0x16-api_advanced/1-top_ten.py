#!/usr/bin/python3
"""
This module queries the reddit api to
find all the subscribers of a subreddit
"""

import requests
# https://www.reddit.com/


def top_ten(subreddit):
    user_agent = "justin"
    headers = {"User-Agent": user_agent}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?Limit=10'
    subreddit_info = requests.get(url, headers=headers, allow_redirects=False)
    if subreddit_info.status_code == 200:
        data = subreddit_info.json()
        result_data = data["data"]["children"]
        for item in result_data[:10]:
            print(item['data']['title'])
    else:
        print(None)
