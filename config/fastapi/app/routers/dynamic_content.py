from fastapi import APIRouter
from sqlalchemy import text

from app.shared_lib.prge_shared.db_conn import engine


router_dynamic_users_from_db = APIRouter()


@router_dynamic_users_from_db.get("/users_dynamic")
async def get_user():
    try:

        sql_query = text("""select id, name, location, posts from users""")

        with engine.connect() as connection:
            result = connection.execute(sql_query)

            users = [dict(row._mapping) for row in result]

        return {"status": "success", "data": users}

    except Exception as e:
        return {"status": f"error {str(e)}"}
