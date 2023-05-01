from enum import Enum
from fastapi import FastAPI, Query

app = FastAPI()

# query string 的接收，直接定義在 function 的參數列上
# http://localhost:8000/?name=david&id=17
@app.get('/')
async def home(id:int=10, name: str="shinder"):
  return {"hello": name, "id": id}

# 資料為 enum 時，先定義類型
class MyFormat(str, Enum):
  LONG='long'
  SHORT='short'

@app.get('/blogs')
async def blog_list(format:MyFormat=MyFormat.SHORT):
  return {"format": format}

# 限定值的範圍
#   gt: Greater than
#   ge: Greater than or equal to
#   lt: Less than
#   le: Less than or equal to
# 以下使用在字串上
#   min_length: 最小長度
#   max_length:: 最大長度
#   regex: 使用 reqex pattern
@app.get('/products')
async def product_list(page:int=Query(1, ge=1), size:int=Query(10, ge=10, le=50)):
  return {'page': page, 'size': size}
