from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/calculate")
async def calculate(expression: str = Form(...)):
    try:
        result = eval(expression)
        return {"result": result}
    except Exception as e:
        return {"result": "Error"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
