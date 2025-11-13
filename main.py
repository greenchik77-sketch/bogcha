from fastapi import FastAPI
from routers.kindergartens import kindergarten_router
from routers.users import user_router

app = FastAPI(title="Bog'cha", docs_url="/")


app.include_router(user_router, tags=["Users"])

app.include_router(kindergarten_router, tags=["Kindergarten"])