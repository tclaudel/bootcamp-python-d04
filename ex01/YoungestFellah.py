from FileLoader import FileLoader


def youngestFellah(data, year):
    filter1 = data["Year"] == year
    filter2 = data["Sex"] == "F"
    woman_data = data.where(filter1 & filter2)
    man_data = data.where(filter1 & -filter2)
    woman_data = woman_data["Age"].min()
    man_data = man_data["Age"].min()
    return {'f': woman_data, 'm': man_data}


loader = FileLoader()
data = loader.load("../athlete_events.csv")
print(youngestFellah(data, 2004))
