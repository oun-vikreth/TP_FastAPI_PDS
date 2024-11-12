from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr

app = FastAPI()

class User(BaseModel):
    name: str
    age: int
    email: EmailStr

@app.post("/users/")
async def create_user(user: User):
    if user.age < 18:
        raise HTTPException(status_code=400, detail="Age must be greater than or equal to 18")

    # Without a database, we can simply return the user data
    return {"message": "User created successfully", "user": user.dict()}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app)