import json
import pandas as pd
from datetime import datetime


def load_json_as_df(
    file: str, include_date=False, include_content=False, include_mentions=False
):
    """Generates a DataFrame with the given specs

    Args:
        file (str): path to json
        include_date (bool, optional): Specifies if the 'date' should be included (tweet date). Defaults to False.
        include_content (bool, optional): Specifies if the 'content' should be included (tweet content). Defaults to False.
        include_mentions (bool, optional): Specifies if the 'mentions' should be included (tweet mentions). Defaults to False.

    Returns:
        type: pd.DataFrame
    """
    data = []
    columns = ["username"]

    if include_date:
        columns.append("date")

    if include_content:
        columns.append("content")

    if include_mentions:
        columns.append("mentions")

    with open(file, encoding="utf-8") as open_file:
        for line in open_file:
            tweet = json.loads(line)
            payload = (tweet["user"]["username"],)

            if include_date:
                date = datetime.strptime(tweet["date"], "%Y-%m-%dT%H:%M:%S%z")
                payload = payload + (date.date(),)

            if include_content:
                payload = payload + (tweet["content"],)

            if include_mentions:
                mention_list = []
                if not tweet["mentionedUsers"] is None:
                    mention_list=[
                    mention["username"] for mention in tweet["mentionedUsers"]
                    ]
                mentions = ", ".join(mention_list)
                payload = payload + (mentions,)

            data.append(payload)

    return pd.DataFrame(data=data, columns=columns)