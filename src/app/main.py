"""FastAPI entrypoint for Raavan AI backend."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api.routes.astrology import router as astrology_router
from src.api.routes.chat import router as chat_router
from src.config.settings import AppConfig


def create_app() -> FastAPI:
    """Create and configure FastAPI application instance."""
    application = FastAPI(
        title=AppConfig.APP_NAME,
        version=AppConfig.APP_VERSION,
        description=AppConfig.APP_DESCRIPTION,
    )

    # CORS middleware keeps the API ready for React/Next.js frontends.
    application.add_middleware(
        CORSMiddleware,
        allow_origins=AppConfig.CORS_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @application.get("/health", tags=["health"])
    def health_check():
        """Health endpoint for deployment checks."""
        return {"status": "ok"}

    application.include_router(chat_router, prefix="/api", tags=["chat"])
    application.include_router(astrology_router, prefix="/api", tags=["astrology"])

    return application


app = create_app()
