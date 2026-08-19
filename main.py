from fastapi import FastAPI
from dotenv import load_dotenv
from routes import base_routes
load_dotenv(".env")
app = FastAPI()
app.include_router(base_routes.User_routes)