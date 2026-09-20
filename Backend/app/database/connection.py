from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

from app.config.settings import DATABASE_URL


engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True
)

SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False
)


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


# Temporary database test
try:
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        print("Database result:", result.scalar())
except Exception as e:
    print("Database connection failed:", e)