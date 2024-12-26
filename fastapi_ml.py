import os
import pickle
from fastapi import FastAPI
from pydantic_BC import Ml_features
import uvicorn
import nest_asyncio
from starlette.responses import FileResponse

# Apply the nest_asyncio patch to allow the event loop to run
nest_asyncio.apply()
# Define FastAPI app
app = FastAPI()
# Load the saved model
pickle_in = open("breast_cancer_model.pkl", "rb")
model = pickle.load(pickle_in)

@app.get('/')
def index():
    return{'message': 'Welcome to Breast Cancer prediction'}

@app.post('/predict')
def predict_bc(data:Ml_features):
    data = data.dict()
    mean_radius = data['mean_radius']
    mean_texture = data['mean_texture']
    mean_perimeter = data['mean_perimeter']
    mean_area = data['mean_area']
    mean_smoothness = data['mean_smoothness']
    prediction = model.predict([[mean_radius, mean_texture, mean_perimeter, mean_area, mean_smoothness]])
    if (prediction[0]==1):
        prediction = 'Malignancy predicted'
    elif(prediction[0]==0):
        prediction = 'You are safe'
    else:
        prediction= 'wrong prediction'
    return {
        'prediction': prediction
    }



async def favicon():
    # Return the favicon.ico file from the root directory
    return FileResponse(os.path.join(os.path.dirname(__file__), "favicon.ico"))

@app.get("/")
def read_root():
    return {"message": "Welcome to the Breast Cancer Prediction API"}


# Run FastAPI using Uvicorn
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
