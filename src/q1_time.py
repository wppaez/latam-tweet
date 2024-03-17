from typing import List, Tuple
from datetime import datetime
from utils import load_json_as_df

def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:
    df = load_json_as_df(file_path, include_date=True)

    tweets_by_date = df.groupby(df['date']).size().reset_index(name='count')

    # Ordena en orden descendente por la cantidad de tweets
    top_10 = tweets_by_date.sort_values(by='count', ascending=False).head(10)

    # Obtén los usuarios con más publicaciones para cada una de las fechas top
    top_10_users= df[df['date'].isin(top_10['date'])].groupby('date')['username'].agg(lambda x: x.value_counts().index[0]).reset_index()

    # Combina los DataFrames para obtener el resultado final
    top_10_users = top_10_users[['date', 'username']]

    return list(top_10_users.itertuples(index=False, name=None))

if __name__ == "__main__":
    result = q1_time('./input/farmers-protest-tweets-2021-2-4.json')
    print(result)