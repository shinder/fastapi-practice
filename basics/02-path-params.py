from enum import Enum
from fastapi import FastAPI, Path

app = FastAPI()

# http://localhost:8000/hello/shinder/26

# 資料類型不符的話會丟出 status 422
# http://localhost:8000/hello/shinder/ab

@app.get('/hello/{name}/{id}')
async def hello(id:int, name: str):
  return {"hello": name, "id": id}

# 資料為 enum 時，先定義類型
class UserType(str, Enum):
  ADMIN='admin'
  GENERAL='general'

@app.get('/user/{type}/{id}')
async def user_type(type:UserType, id:int):
  return {"type": type, "id": id}

# 限定值的範圍
#   gt: Greater than
#   ge: Greater than or equal to
#   lt: Less than
#   le: Less than or equal to
# 以下使用在字串上
#   min_length: 最小長度
#   max_length:: 最大長度
#   regex: 使用 reqex pattern
@app.get('/users/{id}')
async def get_user(id:int=Path(ge=5, le=10)):
  return {"id": id}


