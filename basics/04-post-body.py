from typing import Optional
from pydantic import BaseModel
from fastapi import FastAPI, Request, Response, Body, Form

app = FastAPI()

# query string 的接收，直接定義在 function 的參數列上
# http://localhost:8000/?name=david&id=17
@app.get('/')
async def home(id:int=10, name: str="shinder"):
  return {"hello": name, "id": id}

# Body() 同 Query() 用法
# Body() 只能用在 application/json 的 req 資料
@app.post('/users')
async def user_list(name:str=Body(), age:int=Body(ge=18)):
  return {"name": name, "age": age}

# Body() 第一個參數為預設值
@app.post('/users2')
async def user_list2(name:str=Body('shinder'), age:int=Body(22)):
  return {"name": name, "age": age}

# Form()
@app.post('/users3')
async def user_list2(name:str=Form('shin'), age:int=Form(23)):
  return {"name": name, "age": age}


# 三種不同的格式
@app.post('/')
async def route(req: Request) -> Response:
    if req.headers['Content-Type'] == 'application/json':
        item = await req.json()
    elif req.headers['Content-Type'] == 'multipart/form-data':
        item = await req.form()
    elif req.headers['Content-Type'] == 'application/x-www-form-urlencoded':
        item = await req.form()
    return item


# https://stackoverflow.com/questions/61872923/supporting-both-form-and-json-encoded-bodys-with-fastapi
class MyItem(BaseModel):
  name:str
  age:Optional[int]

@app.post('/2')
async def route2(req: Request) -> Response:
    if req.headers['Content-Type'] == 'application/json':
        item = MyItem(** await req.json())
    elif req.headers['Content-Type'] == 'multipart/form-data':
        item = MyItem(** await req.form())
    elif req.headers['Content-Type'] == 'application/x-www-form-urlencoded':
        item = MyItem(** await req.form())
    return Response(content=item.json())
