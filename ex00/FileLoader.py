import pandas as pd


class FileLoader:
    def load(self, path):
        data = pd.read_csv(path)
        print("Loading dataset of dimensions {0} x {1}".format(data.shape[0],
                                                               data.shape[1]))
        return data

    def display(self, data, n):
        print(data.head(n))


loader = FileLoader()
data = loader.load("../athlete_events.csv")
loader.display(data, 12)
