from fastapi import FastAPI
from contextlib import asynccontextmanager
from watergun.api.brave_web_search_api import BraveWebSearchAPI
from watergun.api.obsidian_api import ObsidianAPI
from watergun.api.fetch_api import FetchAPI
from watergun.api.watergun_server_api import WatergunServerAPI

import logging

logger = logging.getLogger(__name__)


class WatergunServer:
    def __init__(self):
        self.app: FastAPI = self._create_app()
        self._register_routes()
        self._register_middleware()
        self._register_error_handlers()

    def _create_app(self) -> FastAPI:
        @asynccontextmanager
        async def lifespan(app: FastAPI):
            # Startup
            logger.info("🚀 Watergun Server starting up...")
            yield
            # Shutdown
            logger.info("🛑 Watergun Server shutting down...")

        return FastAPI(
            title="Watergun API Server",
            description="Tools server for Open WebUI",
            version="1.0.0",
            lifespan=lifespan,
        )

    def _register_routes(self):
        """
        Register all domain API routes
        """

        BraveWebSearchAPI(self.app).register_routes()
        ObsidianAPI(self.app).register_routes()
        FetchAPI(self.app).register_routes()
        WatergunServerAPI(self.app).register_routes()

    def _register_middleware(self):
        """
        Configure middleware.
        """
        from fastapi.middleware.cors import CORSMiddleware

        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_methods=["*"],
            allow_headers=["*"],
        )

    def _register_error_handlers(self):
        """
        Register global error handlers.
        """
        from watergun.server.error_handlers import ErrorHandlers

        er = ErrorHandlers(self.app)
        er.register_error_handlers()


_server = WatergunServer()
app = _server.app
