from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/")
async def root() -> dict[str, str]:
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
async def read_item(item_id) -> str:
    # return {"item_id": item_id}
    html_body = f'<div>item_id : {item_id}</div>'
    return HTMLResponse(content=html_body, status_code=200)

