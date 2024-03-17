from typing import List, Tuple
from utils import load_json_as_df
from collections import Counter

def q3_memory(file_path: str) -> List[Tuple[str, int]]:
    # Load JSON data into DataFrame
    df = load_json_as_df(file_path, include_mentions=True)

    # Use Counter to count mentions directly in DataFrame
    mention_counter = Counter(df['username'])

    # Sort users by mention count in descending order
    sorted_mentions = sorted(mention_counter.items(), key=lambda x: x[1], reverse=True)

    # Return top 10 users with mention counts
    top_10_users = sorted_mentions[:10]
    return top_10_users

if __name__ == "__main__":
    result = q3_memory('./input/farmers-protest-tweets-2021-2-4.json')
    print(result)
