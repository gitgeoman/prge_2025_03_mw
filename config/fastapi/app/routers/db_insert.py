from fastapi import APIRouter
from sqlalchemy import create_engine, text
from pydantic import BaseModel

from app.settings import db_name, db_user, db_password

router_db_insert = APIRouter()


class UserData(BaseModel):
    name: str
    posts: int
    location: str


@router_db_insert.post("/insert_user")
async def insert_user(user: UserData):
    try:
        connection_string = f"postgresql://{db_user}:{db_password}@postgis:5432/{db_name}"
        engine = create_engine(connection_string)

        params = {
            "name": user.name,
            "posts": user.posts,
            "location": user.location,
        }

        sql_query = text("""
                         insert into users (name, posts, location)
                         values (:name, :posts, :location);
                         """)

        with engine.connect() as connection:
            results = connection.execute(sql_query, params)
            connection.commit()
            print(results)

        return {"status": "success", "data_inserted": {user.name, user.posts, user.location}}


    except Exception as e:
        return {"status": f"error {str(e)}"}
