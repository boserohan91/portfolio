from fastapi import FastAPI
from src.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get('/')
def root():
    return {'This is the root page'}