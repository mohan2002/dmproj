from fastapi import FastAPI
import pickle

app = FastAPI()
pickle_in = open("predictor.pkl","rb")
coursedatas = pickle.load(pickle_in)

@app.get('/')
async def hello():
    return coursedatas