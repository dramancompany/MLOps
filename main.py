from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.router import test, predict, train, upload
from app.database import SessionLocal

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(test.router)
app.include_router(predict.router)
app.include_router(upload.router)
app.include_router(train.router)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def hello_world():
    return {"message": "Hello World"}
