from fastapi import APIRouter
import os
import importlib

router = APIRouter()

def load_routers():
    current_dir = os.path.dirname(__file__)
    for filename in os.listdir(current_dir):
        if filename.endswith(".py") and filename != "__init__.py":
            module_name = f"{__name__}.{filename[:-3]}"  # Full module path
            module = importlib.import_module(module_name)
            if hasattr(module, "router"):
                router.include_router(module.router)


load_routers()