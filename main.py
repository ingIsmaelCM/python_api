from fastapi import FastAPI
from dotenv import load_dotenv
from app.models.user_model import UserModel

app = FastAPI()
load_dotenv()


@app.get('/')
async def say_hell():
    try:
        user = UserModel.get_by_id(1)
        print(user)
        return 2 + 4 * 7
    except Exception as e:
        print(e)
