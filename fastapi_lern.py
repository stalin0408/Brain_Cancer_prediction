import uvicorn
from fastapi import FastAPI

#create the app object
app = FastAPI()
@app.get('/')
def index():
    return {'message':'Hello, Stranger'}
@app.get('/Welcome')
def welcome(name: str):
    return {'Welcome to fist app': f'{name}'}


#running the api
if __name__=='__main__':
    uvicorn.run(app, host='127.0.0.1', port= 8000)
