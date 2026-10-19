"""
===============================================================================
WHAT: Base API Router
OVERVIEW: Defines the entry endpoints (like the welcome route) for the API v1.
HOW IT WORKS: Uses FastAPI's `APIRouter` to group related routes and uses 
              `Depends()` to inject the app settings securely into the functions.
WHY: Keeps API routes modular and organized. Using `Depends` for settings 
     makes the code easier to test (via mock dependencies) and optimizes performance.
===============================================================================
"""

from fastapi import FastAPI, APIRouter
import os
from helpers.config import get_settings

base_router = APIRouter(
    prefix="/rag_api/v1",
    tags=["api_v1"]
)

@base_router.get("/")
async def welcome_guest():
    app_settings = get_settings()
    app_name= app_settings.APP_NAME
    app_version= app_settings.APP_VERSION
    return {
            "app_name": app_name,
            "app_version": app_version
        }