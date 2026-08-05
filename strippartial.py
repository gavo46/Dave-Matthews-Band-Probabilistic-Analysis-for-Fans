import pandas as pd

data = pd.read_csv("allshows.csv")
data["Song"] = data["Song"].str.replace(r"\s*\[partial\]", "", regex=True, case=False)  
data["Last Played"] = data["Last Played"].str.replace(", LIB", "") 
data.to_csv("allshows.csv", index=False)     