import pandas as pd
import emoji
from typing import List, Tuple
from utils import load_json_as_df

def extract_emojis(text: str) -> List[str]:
    return [c for c in text if c in emoji.EMOJI_DATA]

def q2_time(file_path: str) -> List[Tuple[str, int]]:
    df = load_json_as_df(file_path, include_content=True)
    
    # Crear un conjunto de emojis únicos
    unique_emojis = set(emoji.EMOJI_DATA.keys())
    
    # Contar emojis únicos en cada texto
    emojis_count = {}
    for text in df['content']:
        extracted_emojis = set(extract_emojis(text))  # Convertir a conjunto para emojis únicos
        emojis_in_text = extracted_emojis.intersection(unique_emojis)  # Filtrar emojis válidos
        for current_emoji in emojis_in_text:
            emojis_count[current_emoji] = emojis_count.get(current_emoji, 0) + 1
    
    # Obtener los 10 emojis más frecuentes
    top_emojis = sorted(emojis_count.items(), key=lambda x: x[1], reverse=True)[:10]
    return top_emojis

if __name__ == "__main__":
    result = q2_time('./input/farmers-protest-tweets-2021-2-4.json')
    print(result)
