from FileLoader import FileLoader


def proportionBySport(data, year, sport, gender):
    filter1 = data["Year"] == year
    filter2 = data["Sport"] == sport
    filter3 = data["Sex"] == gender
    found_array = data[filter1 & filter2 & filter3]
    found_array = found_array.drop_duplicates(subset="Name", keep="first")
    data = data[filter1 & filter3].drop_duplicates(subset="Name", keep="first")
    return len(found_array) / len(data)


loader = FileLoader()
data = loader.load("../athlete_events.csv")
print(proportionBySport(data, 2004, 'Tennis', 'F'))
