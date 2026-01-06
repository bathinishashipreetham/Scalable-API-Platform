from fastapi import FastAPI
from app.core.config import settings
from app.core.database import Base, engine
from app.auth.routes import router as auth_router
from app.auth.dependencies import get_current_user
from fastapi import Depends

@app.get("/me")
def read_me(current_user: str = Depends(get_current_user)):
    return {"email": current_user}


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.app_name,
    version=settings.api_version,
    description="Production-grade backend system built with FastAPI",
)

app.include_router(auth_router)


@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "ok"}

