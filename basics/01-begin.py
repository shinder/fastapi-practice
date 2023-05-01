from fastapi import FastAPI

app = FastAPI()

@app.get('/hello')
async def hello()->dict:
  return {"say": "hello", "shin": "der"}
