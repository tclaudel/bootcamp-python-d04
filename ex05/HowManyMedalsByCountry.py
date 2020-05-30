from FileLoader import FileLoader

def howManyMedalsByCountry(data, country_name):
    filter1 = data["Team"] == country_name
    filter2 = data["Medal"]
    data = data[filter1 & filter2]
    data = data.set_index("Year")
    data["M"] = data["Medal"].str[:1]
    grouped = data.groupby(['Year'])
    grouped = grouped.M.value_counts()
    unstacked = grouped.unstack(fill_value=0)
    # print(unstacked.apply(int))
    return unstacked.to_dict(orient='index')

loader = FileLoader()
data = loader.load("../athlete_events.csv")
print(howManyMedalsByCountry(data, 'China'))