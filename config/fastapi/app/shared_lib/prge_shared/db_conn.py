from sqlalchemy import create_engine, text
from app.settings import db_name, db_user, db_password

engine = create_engine(f"postgresql://{db_user}:{db_password}@postgis:5432/{db_name}")