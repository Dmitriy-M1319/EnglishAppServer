from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
def index():
    html_content = "<h2>Hello METANIT.COM!</h2>"
    return HTMLResponse(content=html_content)
