from typing import List, Tuple
from utils import load_json_as_df

def q3_time(file_path: str) -> List[Tuple[str, int]]:
    # Load JSON data into DataFrame
    df = load_json_as_df(file_path, include_mentions=True)

    # Extract usernames and count mentions
    user_mentions = df['username'].value_counts().items()

    # Sort users by mention count in descending order
    sorted_mentions = sorted(user_mentions, key=lambda x: x[1], reverse=True)

    # Return top 10 users with mention counts
    top_10_users = sorted_mentions[:10]
    return top_10_users

if __name__ == "__main__":
    result = q3_time('./input/farmers-protest-tweets-2021-2-4.json')
    print(result)
