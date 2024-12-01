from typing import Annotated
from fastapi import FastAPI, Path


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Главная страница"}

@app.get("/user/admin")
async def admin():
    return{"Вы вошли как администратор"}

@app.get("/user/{user_id}")
async def user_id(user_id:Annotated[int,Path(gt=1,gl=100, title='Enter User ID')]):
    return {f"Вы вошли как пользователь №": user_id}

@app.get("/user/{username}/{age}")
async def user(username:Annotated[str,Path(min_length=5, max_length=20, title="Enter username" )],
               age:Annotated[int,Path(gt=18, ge=120,title="Enter age")]):
    return {"Информация о пользователе. Имя": username, "Возраст": age}



