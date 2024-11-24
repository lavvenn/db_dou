from fastapi import FastAPI

from pydantic import BaseModel  


from  db import add_child, print_children




app = FastAPI()

@app.get("/")
async def root():
    children = print_children()

    return {"message": str(children)}