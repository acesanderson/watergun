from fastapi import FastAPI


class ObsidianAPI:
    def __init__(self, app: FastAPI):
        self.app: FastAPI = app

    def register_routes(self):
        """
        Register all conduit routes
        """

        @self.app.get("/obsidian/get_obsidian_doc")
        async def get_obsidian_doc(filename: str) -> str:
            from watergun.services.obsidian_service.get_obsidian_doc_service import (
                get_obsidian_doc_service,
            )

            return await get_obsidian_doc_service(filename)
