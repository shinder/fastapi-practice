# fastapi-practice

## 環境

可以在 conda 環境或 venv 中，先安裝以下三個套件。

```sh
pip install fastapi
pip install uvicorn  # ASGI server
pip install gunicorn  # WSGI server

# 解析表單資料要裝 python-multipart
pip install python-multipart
```

## 開發環境啟動

每個子資料夾皆為一主題練習。進入子資料夾，以下列命令列啟動。

```sh
# 開發啟動
uvicorn main:app --reload --port 8888
# 預設為 port 8000
uvicorn 01-begin:app --reload
uvicorn 02-path-params:app --reload
uvicorn 03-query-string:app --reload
uvicorn 04-post-body:app --reload

# 開發啟動，使用 gunicorn
gunicorn main:app -b 0.0.0.0:8888 -k uvicorn.workers.UvicornWorker

# 使用 Nodejs pm2 啟動
pm2 --name=gunicorn start "gunicorn main:app -b 0.0.0.0:8888 -k uvicorn.workers.UvicornWorker"
```
