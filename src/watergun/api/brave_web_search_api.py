from fastapi import FastAPI


class BraveWebSearchAPI:
    def __init__(self, app: FastAPI):
        self.app: FastAPI = app

    def register_routes(self):
        """
        Register all conduit routes
        """

        @self.app.get("/search/brave_web_search")
        async def brave_web_search(query: str, page: int = 1) -> str:
            from watergun.services.brave_web_search_service import (
                brave_web_search_service,
            )

            return await brave_web_search_service(query, page)
