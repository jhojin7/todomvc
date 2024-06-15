from fastapi import FastAPI, Body, Request, Form
from fastapi.responses import HTMLResponse, FileResponse, JSONResponse, RedirectResponse
from db import get_all_tasks, add_one_task
from typing import Annotated

app = FastAPI()

@app.get("/")
def main():
    return FileResponse("static/index.html")

@app.get("/tasks")
def list_tasks():
    tasks = get_all_tasks(sort_by_newest=True)
    return JSONResponse(tasks,200)

@app.post("/tasks")
def add_task(
    content:Annotated[str, Form()]
):
    resp = add_one_task(content)
    if resp:
        return JSONResponse({"error":str(resp),"content":str(content)},200)
    return FileResponse("static/index.html")
