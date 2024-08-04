from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
from starlette.responses import HTMLResponse
from controllers.user_controller import user_router
from controllers.health_controller import health_router
from db.init_db import init_db

app = FastAPI()

# Register API routers
app.include_router(user_router, prefix="/users")
app.include_router(health_router, prefix="/health")

# Set up template directory
templates = Jinja2Templates(directory="templates")

@app.on_event("startup")
def on_startup():
    init_db()
@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "message": "Hello World"})

