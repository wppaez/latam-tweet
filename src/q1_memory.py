from typing import List, Tuple
from datetime import datetime
from utils import load_json_as_df
import pandas as pd

def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
    # Cargar el DataFrame directamente en lugar de cargarlo y luego agruparlo
    df = load_json_as_df(file_path, include_date=True)

    # Obtener las fechas con más tweets directamente sin agrupar todo el DataFrame
    top_dates = df['date'].value_counts().head(10).index

    # Filtrar el DataFrame solo para las fechas con más tweets
    top_df = df[df['date'].isin(top_dates)]

    # Obtener los usuarios con más publicaciones para cada fecha top
    top_users = top_df.groupby('date')['username'].agg(lambda x: x.value_counts().idxmax()).reset_index()

    # Convertir las fechas a objetos datetime.date
    top_users['date'] = pd.to_datetime(top_users['date']).dt.date

    # Obtener el resultado final como una lista de tuplas
    result = list(top_users.itertuples(index=False, name=None))

    return result

if __name__ == "__main__":
    result = q1_memory('./input/farmers-protest-tweets-2021-2-4.json')
    print(result)
