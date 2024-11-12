from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def hello_name(name: str):
    return {"Hello": name}

@app.get("/hello/{name}")
async def hello_name_age(name: str, age: int = None):
    if age:
        return {"message": f"Hello, {name}! You are {age} years old."}
    return {"message": f"Hello, {name}!"}


# if __name__ == "__main__":
#     import uvicorn

#     uvicorn.run(app)