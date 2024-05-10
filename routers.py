from fastapi import FastAPI, HTTPException
from models import User, UserUpdate, List
from data import db_users

app = FastAPI()


@app.get("/users/", response_model=List[User])
async def get_users():
    return db_users


@app.get("/users/{user_id}", response_model=User)
async def get_user_by_id(user_id: int):
    user = next((user for user in db_users if user.id == user_id), None)
    if not user is None:
        return user
    else:
        raise HTTPException(status_code=404, detail="User not found")


@app.post("/users/", response_model=User)
async def create_user(user: User):
    db_users.append(user)
    return user


@app.put("/users/{user_id}", response_model=UserUpdate)
async def update_user(user_id: int, user: UserUpdate):
    usr = next((u for u in db_users if u.id == user_id), None)
    print(usr)
    if not usr is None:
        if user.username:
            usr.username = user.username
        if user.wallet:
            usr.wallet = user.wallet
        if user.birthdate:
            usr.birthdate = user.birthdate
        return usr
    else:
        raise HTTPException(status_code=404, detail="User not found")


@app.delete("/users/{user_id}", response_model=User)
async def delete_user(user_id: int):
    user_pos = next((i for i, u in enumerate(db_users) if u.id == user_id), None)
    if not user_pos is None:
        print(user_pos)
        user_val = db_users.pop(user_pos)
        return user_val
    else:
        raise HTTPException(status_code=404, detail="User not found")