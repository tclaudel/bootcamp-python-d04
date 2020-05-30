from FileLoader import FileLoader

class SpatioTemporalData:
    def __init__(self, data):
        self.data = data

    def when(self, location):
        filter = self.data["City"] == location
        return self.data[filter].drop_duplicates(subset="Year").Year.to_list()

    def where(self, date):
        filter = self.data["Year"] == date
        return self.data[filter].drop_duplicates(subset="City").City.to_list()
    # def where(selfself, date):


loader = FileLoader()
data = loader.load("../athlete_events.csv")
sp = SpatioTemporalData(data)
print(sp.when('Athina'))
print(sp.when('Paris'))
print(sp.where(1896))
print(sp.where(2016))