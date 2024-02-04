import random
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def root() -> dict[str, str]:
    html_body = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>experiments/htmx ul</title>
    <script src="/static/htmx.min.js"></script> 
    <link rel="stylesheet" href="/static/styles.css" >
</head>
<body>
    <h1>experiments/htmx ul</h1>
    <button hx-get="/ul" hx-target="#list" hx-swap="beforeend scroll:bottom">add another ul</button>
    <ul id="list">
        <li>first one</li>
    </ul>
</body>
</html>
    '''
    return HTMLResponse(content=html_body, status_code=200)

@app.get('/ul')
async def ul():
    return HTMLResponse(content=f'<li>{random.randint(100000, 999999)}</li>')

@app.get("/items/{item_id}")
async def read_item(item_id) -> str:
    # return {"item_id": item_id}
    html_body = f'<div>item_id : {item_id}</div>'
    return HTMLResponse(content=html_body, status_code=200)

