from fastapi import APIRouter

router = APIRouter()


@router.get("/users_static")
async def get_user():
    return [
        {"id": 1, "name": "Mikołaj", "location": "Kielce", "posts": 10},
        {"id": 2, "name": "Adam", "location": "Szczecin", "posts": 20},
        {"id": 3, "name": "Rafał", "location": "Turek", "posts": 30},
        {"id": 4, "name": "Piotr", "location": "Garwolin", "posts": 15},
        {"id": 5, "name": "Ola", "location": "Białystok", "posts": 123},
    ]
