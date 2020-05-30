from FileLoader import FileLoader
import pandas as pd


def howManyMedals(data, name):
    filer1 = data["Name"] == name
    filer2 = data["Medal"]
    data = data[filer1 & filer2]
    data = data.set_index("Year")
    data["M"] = data["Medal"].str[:1]
    grouped = data.groupby(['Year'])
    grouped = grouped.M.value_counts()
    unstacked = grouped.unstack(fill_value=0)
    return unstacked.to_dict(orient='index')


loader = FileLoader()
data = loader.load("../athlete_events.csv")
print(howManyMedals(data, 'Kjetil Andr Aamodt'))