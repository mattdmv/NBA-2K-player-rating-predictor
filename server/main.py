# libraries imports
from fastapi import FastAPI, Form
import uvicorn
from pydantic import BaseModel
import pickle
import utility

# create the app object
app = FastAPI()

# load the model
#pickle_in = open ('/artifacts/NBA2K_player_rating_prediction_model.pickle', 'rb')
#model = pickle.load(pickle_in)

@app.post('/predict_player_rating')
async def predict_player_rating(player_name: str):

    response = utility.main_pipeline(player_name)

    return {'predicted_value':response}

if __name__=="__main__":
    print("Starting FastAPI Server for NBA2K player rating prediction!")
    uvicorn.run(app, host='localhost', port=8000)

