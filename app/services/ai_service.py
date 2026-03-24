import os
from ml_model import model_v1, model_v2
from app.db.redis_client import redis_client

MODEL_VERSION = os.getenv("MODEL_VERSION", "v1")

def get_response(query):
   
    cached = redis_client.get(query)
    if cached:
        return f"(cached) {cached}"

    if MODEL_VERSION == "v2":
        response = model_v2.predict(query)
    else:
        response = model_v1.predict(query)

    redis_client.setex(query, 60, response)  # expires in 60 sec

    return response