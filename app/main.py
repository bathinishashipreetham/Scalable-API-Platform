from fastapi import FastAPI
from app.core.config import settings
from app.core.database import Base, engine
from app.auth.routes import router as auth_router

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

