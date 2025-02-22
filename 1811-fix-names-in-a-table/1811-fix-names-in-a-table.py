import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    users.sort_values(by='user_id',inplace=True)
    users['name']=users['name'].str.capitalize() 
    return users  