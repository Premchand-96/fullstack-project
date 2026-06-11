from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy import text
from database import engine

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class User(BaseModel):
    id: int
    name: str
    email: str
    role: str

@app.get("/")
def home():
    return {"message": "FastAPI Backend Running"}

@app.get("/api/users")
def get_users():

    connection = engine.connect()

    query = text("SELECT * FROM users")

    result = connection.execute(query)

    users = []

    for row in result:
        users.append({
            "id": row[0],
            "name": row[1],
            "email": row[2],
            "role": row[3]
        })

    connection.close()

    return users

@app.post("/api/users")
def create_user(user: User):

    connection = engine.connect()

    connection.execute(
        text("""
            INSERT INTO users(id, name, email, role)
            VALUES(:id, :name, :email, :role)
        """),
        {
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "role": user.role
        }
    )

    connection.commit()
    connection.close()

    return {"message": "User inserted successfully"}
