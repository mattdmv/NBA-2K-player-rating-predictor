import pickle
import json
import numpy as np

__data_columns = None
__model = None

def get_estimated_rating(pts,reb,ast,stl,blk,three_p,plus_minus,gp):
    
    x = np.zeros(len(__data_columns))
    x[0] = pts
    x[1] = reb
    x[2] = ast
    x[3] = stl
    x[4] = blk
    x[5] = three_p
    x[6] = plus_minus
    x[7] = gp

    return round(__model.predict([x])[0],2)


def load_saved_artifacts():
    print("Start loading saved artifacts!")
    global  __data_columns

    with open("./artifacts/final_columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        
    global __model
    if __model is None:
        with open('./artifacts/NBA2K_player_rating_prediction_model.pickle', 'rb') as f:
            __model = pickle.load(f)
    print("Saved artifacts loaded sucessfully!")

def get_data_columns():
    return __data_columns

if __name__ == '__main__':
    load_saved_artifacts()