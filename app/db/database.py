from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import time

DATABASE_URL = "postgresql://admin:admin@postgres-db:5432/hotel"

# 🔥 Retry logic
for i in range(10):
    try:
        engine = create_engine(DATABASE_URL)
        connection = engine.connect()
        print("✅ Connected to DB")
        connection.close()
        break
    except Exception as e:
        print("⏳ DB not ready, retrying...")
        time.sleep(3)

SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()