from sqlalchemy import create_engine, String, BIGINT
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

engine = create_engine("postgresql+psycopg2://postgres:99@172.17.0.2:5432/restaurant_db")

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"
    user_id: Mapped[int] = mapped_column(BIGINT, primary_key=True)
    username: Mapped[String] = mapped_column(String(100))



Base.metadata.create_all(engine)