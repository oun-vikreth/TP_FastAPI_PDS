from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # <-- Change "*" to specific domains like ["http://127.0.0.1:5500"] for better security
    allow_credentials=True,
    allow_methods=["*"],  # Allows GET, POST, PUT, DELETE, etc.
    allow_headers=["*"],  # Allows all headers
)

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