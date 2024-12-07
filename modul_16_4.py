from fastapi import FastAPI, Path, HTTPException
from typing import Annotated
from pydantic import BaseModel
from typing import List

class User(BaseModel):
    id: int
    username:str
    age: int

app = FastAPI()

users = []

@app.get('/users')
async def get_users() -> List[User]:
    return users

@app.post('/user/{username}/{age}')
async def get_new_user(username:Annotated[str,Path(min_length=5, max_length=20,
                                                   title="Enter username",example="")],
                       age:Annotated[int,Path(ge=18, le=100,title="Enter age", example="")])-> User:
    if not users:
        new_user = User(id=1, username=username, age=age)
    else:
        new_user = User(id=users[-1].id+1, username=username, age=age)
    users.append(new_user)
    return new_user

@app.put('/user/{user_id}/{username}/{age}')
async def get_update(user_id: Annotated[int, Path(ge=0,
                                             le=20,
                                             description='Enter id',
                                             example='1')],
                   username: Annotated[str, Path(min_length=5,
                                                 max_length=20,
                                                 description='Enter username',
                                                 example='UrbanUser')],
                   age: Annotated[int, Path(ge=18,
                                            le=100,
                                            description='Enter age',
                                            example='24')]) -> User:
    try:
        new_user = users[user_id - 1]
        new_user.username = username
        new_user.age = age
        return new_user
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")


@app.delete('/user/{user_id}')
async def get_delete_user(user_id: Annotated[int, Path(ge=0,
                                             le=20,
                                             description='Enter id',
                                             example='1')]) -> User:
    try:
        new_user = users[user_id - 1]
        users.pop(user_id - 1)
        return new_user
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")