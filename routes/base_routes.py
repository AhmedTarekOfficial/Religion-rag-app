from fastapi import APIRouter
import os 

User_routes = APIRouter(tags=["Foundation"] , prefix="/foundation")

@User_routes.get("/Greatings" )
def Greatings():
    app_name = os.getenv("APP_NAME")
    app_version = os.getenv("APP_VERSION")
    return f"Hello, {app_name} v{app_version}!"

