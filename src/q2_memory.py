import pandas as pd
import emoji
from typing import List, Tuple
from utils import load_json_as_df

def extract_emojis(text: str) -> List[str]:
    return [c for c in text if c in emoji.EMOJI_DATA]

def q2_memory(file_path: str) -> List[Tuple[str, int]]:
    df = load_json_as_df(file_path, include_content=True)
    emojis_count = {}
    for text in df['content']:
        emojis = extract_emojis(text)
        for emoji in emojis:
            emojis_count[emoji] = emojis_count.get(emoji, 0) + 1
    top_emojis = sorted(emojis_count.items(), key=lambda x: x[1], reverse=True)[:10]
    return top_emojis

if __name__ == "__main__":
    result = q2_memory('./input/farmers-protest-tweets-2021-2-4.json')
    print(result)
