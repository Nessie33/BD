from fastapi import FastAPI, HTTPException


app = FastAPI()


users = {'1': 'Имя: Example, возраст: 18'}


@app.get('/users')
async def one() -> dict:
    return users


@app.post('/user/{username}/{age}')
async def two(username: str, age: int) -> str:
    user_id = str(max(map(int, users.keys()), default=0) + 1)
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f"User {user_id} is registered"


@app.put('/user/{user_id}/{username}/{age}')
async def three(user_id: str, username: str, age: int) -> str:
    if user_id not in users:
        raise HTTPException(status_code=404, detail='Задача не найдена')
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f"The user {user_id} is updated"


@app.delete('/user/{user_id}')
async def four(user_id: str):
    if user_id not in users:
        raise HTTPException(status_code=404, detail='Задача не найдена')
    del users[user_id]
    return f"User {user_id} has been deleted"