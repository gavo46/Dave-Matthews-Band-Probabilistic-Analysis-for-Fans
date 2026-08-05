import pandas as pd
data = pd.read_csv("allshows.csv")
print(data.duplicated().sum())  # how many exact duplicate rows exist
print(data[data["Song"] == "kit kat jam"])  # eyeball this song's actual rows