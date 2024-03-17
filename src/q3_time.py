from typing import List, Tuple
from utils import load_json_as_df
from collections import Counter

def q3_time(file_path: str) -> List[Tuple[str, int]]:
    # Load JSON data into DataFrame
    df = load_json_as_df(file_path, include_mentions=True)

    # Use Counter to count mentions directly in DataFrame
    mention_counter = Counter(df['username'])

    # Get top 10 users with mention counts
    top_10_users = mention_counter.most_common(10)
    return top_10_users

if __name__ == "__main__":
    result = q3_time('./input/farmers-protest-tweets-2021-2-4.json')
    print(result)
