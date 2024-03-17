import pandas as pd
import emoji
from typing import List, Tuple
from utils import load_json_as_df

def extract_emojis(text: str):
    for c in text:
        if c in emoji.EMOJI_DATA:
            yield c

def q2_memory(file_path: str) -> List[Tuple[str, int]]:
    emojis_count = {}
    batch_size = 1000  # Procesa el archivo por lotes de 1000 tweets
    for chunk in pd.read_json(file_path, lines=True, chunksize=batch_size):
        for text in chunk['content']:
            emojis = extract_emojis(text)
            for emoji in emojis:
                emojis_count[emoji] = emojis_count.get(emoji, 0) + 1
    top_emojis = sorted(emojis_count.items(), key=lambda x: x[1], reverse=True)[:10]
    return top_emojis

if __name__ == "__main__":
    result = q2_memory('./input/farmers-protest-tweets-2021-2-4.json')
    print(result)
