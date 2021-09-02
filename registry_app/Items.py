
from os.path import abspath, dirname, exists
from pandas import read_csv, DataFrame
import pickle

class Items(dict):

    def __init__(self, reset_pickle=False, update_pickle=False):
        self._base_path = f"{dirname(abspath(__file__))}/static/dta/"
        self._csv_path = self._base_path + "items.txt"
        self._pickle_path = self._base_path + "items.pickle"
        self._items_df = read_csv(self._csv_path, sep='\t')
        self._items_df["purchased"] = 0
        self._items_df.fillna(" ", inplace=True)

        if reset_pickle or not exists(self._pickle_path):
            self._items_dict = self._items_df.to_dict(orient="index")
            self.pickle_items()
        elif update_pickle:
            pickle_df = DataFrame.from_dict(self.unpickle_items(), orient="index")
            i = pickle_df.index.max() + 1
            while i <= self._items_df.index.max():
                pickle_df.loc[i] = self._items_df.loc[i]
                i += 1
            self._items_dict = pickle_df.to_dict(orient="index")
            self.pickle_items()
        else:
            self._items_dict = self.unpickle_items()

    def pickle_items(self):
        with open(self._pickle_path, 'wb') as handle:
            pickle.dump(self._items_dict, handle)

    def unpickle_items(self):
        with open(self._pickle_path, 'rb') as handle:
            return pickle.load(handle)

    def get_items(self):
        return self._items_dict

    def update_item_as_purchased(self, item_index):
        self._items_dict[item_index]["purchased"] = 1
        self.pickle_items()
        return self.get_items()

    def update_item_as_not_purchased(self, item_index):
        self._items_dict[item_index]["purchased"] = 0
        self.pickle_items()
        return self.get_items()
