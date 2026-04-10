from fastapi import FastAPI


class FetchAPI:
    def __init__(self, app: FastAPI):
        self.app: FastAPI = app

    def register_routes(self):
        """
        Register all conduit routes
        """

        @self.app.get(
            "/fetch/fetch_url",
            summary="Fetch a URL and return its content",
            description="Fetch a URL and return its content; this has fallbacks, cloudflare bypass, and even headless browser support with playwright",
        )
        async def fetch_url(url: str, page: int = 1) -> str:
            from watergun.services.fetch_service.fetch_url_service import (
                fetch_url_service,
            )

            return await fetch_url_service(url, page)
