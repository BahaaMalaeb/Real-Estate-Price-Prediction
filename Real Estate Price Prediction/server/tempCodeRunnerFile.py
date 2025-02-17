import pickle
import json
import numpy as np

__city = None
__data_columns = None
__model = None

def get_estimated_price(bedrooms,bathrooms,sqft_living,floors,condition,city):
    try:
        loc_index = __data_columns.index(city.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = bedrooms
    x[1] = bathrooms
    x[2] = sqft_living
    x[3] = floors
    x[4] = condition
    if loc_index>=0:
        x[loc_index] = 1

    return round(__model.predict([x])[0],2)


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global  __data_columns
    global __locations

    with open("./artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[5:]

    global __model
    if __model is None:
        with open('./artifacts/home_prices_model.pickle', 'rb') as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")

def get_location_names():
    return __locations

def get_data_columns():
    return __data_columns

if __name__ == '__main__':
  load_saved_artifacts()
  get_estimated_price(2,1,1000,1,3,"maple valley")
  get_estimated_price(3,2,2000,2,4,"maple valley")
  get_estimated_price(3,2,2000,2,2,"maple valley")

  get_estimated_price(3,2,2000,2,1,"maple valley")


