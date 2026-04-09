from fastapi import APIRouter
from sqlalchemy import create_engine, text

from app.settings import db_name, db_user, db_password

router_dynamic_users_from_db = APIRouter()


@router_dynamic_users_from_db.get("/users_dynamic")
async def get_user():
    try:
        connection_string = f"postgresql://{db_user}:{db_password}@postgis:5432/{db_name}"
        engine = create_engine(connection_string)

        sql_query = text("""select id, name, location, posts from users""")

        with engine.connect() as connection:
            result = connection.execute(sql_query)

            users = [dict(row._mapping) for row in result]

        return {"status": "success", "data": users}

    except Exception as e:
        return {"status": f"error {str(e)}"}
