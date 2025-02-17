import warnings

warnings.filterwarnings("ignore", message=".*does not have valid feature names.*")


import pickle
import json
import numpy as np
import os

__city = None
__data_columns = None
__model = None

def get_estimated_price(bedrooms, bathrooms, sqft_living, floors, condition, city):
    try:
        loc_index = __data_columns.index(city.lower())
    except ValueError:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = bedrooms
    x[1] = bathrooms
    x[2] = sqft_living
    x[3] = floors
    x[4] = condition
    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0], 2)

def load_saved_artifacts():
    print("Loading saved artifacts... start")
    global __data_columns
    global __locations
    global __model

    base_dir = os.path.dirname(__file__)
    columns_path = os.path.join(base_dir, "artifacts", "columns.json")
    model_path = os.path.join(base_dir, "artifacts", "home_prices_model.pickle")

    with open(columns_path, "r") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[5:]

    with open(model_path, 'rb') as f:
        __model = pickle.load(f)
    
    print("Loading saved artifacts... done")

def get_location_names():
    return __locations

def get_data_columns():
    return __data_columns

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_estimated_price(2, 1, 1000, 1, 3, "maple valley"))
    print(get_estimated_price(3, 2, 2000, 2, 4, "maple valley"))
    print(get_estimated_price(3, 2, 2000, 2, 2, "maple valley"))
    print(get_estimated_price(3, 2, 2000, 2, 1, "maple valley"))
