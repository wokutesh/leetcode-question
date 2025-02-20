import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    df=animals[animals['weight']>100]
    df1=df.sort_values(by=['weight'],ascending=False)
    return df1[['name']]